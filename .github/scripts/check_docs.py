"""Check this documentation package without third-party Python dependencies.

Run from the exported repository root. --site also validates Jekyll output.
External URL availability and product behavior are outside this check's scope.
"""

import argparse
import os
import html
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[2]
ERRORS = []


def fail(message):
    ERRORS.append(message)


def scalar(config, name):
    match = re.search(rf"^{re.escape(name)}:\s*(.+)$", config, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing configuration: {name}")
    return match.group(1).strip().strip("\"'")


def exact_file(root, relative):
    """Check casing even on a case-insensitive filesystem."""
    current = root
    for part in relative.parts:
        if part in ("", "."):
            continue
        if part == ".." or not current.is_dir():
            return False
        names = {entry.name for entry in current.iterdir()}
        if part not in names:
            return False
        current /= part
    return current.is_file()


def headings(markdown):
    ids = set()
    seen = {}
    in_code = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if match:
            title = html.unescape(match.group(1)).lower()
            slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            ids.add(f"{slug}-{count}" if count else slug)
    return ids


def check_sources():
    sources = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
    sources.append(ROOT / ".github/MAINTAINERS.md")
    contents = {path: path.read_text(encoding="utf-8") for path in sources}
    anchors = {path: headings(value) for path, value in contents.items()}
    count = 0
    for path, value in contents.items():
        label = path.relative_to(ROOT).as_posix()
        if "\u2014" in value:
            fail(f"{label}: contains an em dash")
        if path.parent.name != ".github" and not value.startswith("---\n"):
            fail(f"{label}: missing page metadata")
        if path.parent.name == "docs" and "../README.md" not in value:
            fail(f"{label}: missing overview link")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", value):
            count += 1
            target = target.strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith("/"):
                fail(f"{label}: Markdown link must be relative: {target}")
                continue
            destination = Path(os.path.abspath(path.parent / unquote(url.path))) if url.path else path
            try:
                relative = destination.relative_to(ROOT)
            except ValueError:
                fail(f"{label}: link escapes the package: {target}")
                continue
            if not exact_file(ROOT, relative):
                fail(f"{label}: missing file or wrong casing: {target}")
            elif url.fragment and destination.suffix == ".md":
                if unquote(url.fragment) not in anchors.get(destination, set()):
                    fail(f"{label}: unknown heading anchor: {target}")
    print(f"Source check: {len(sources)} Markdown files, {count} links inspected.")


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.canonical = []
        self.h1_count = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        for name in ("href", "src"):
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))


def check_site(site, origin, prefix):
    site = site.resolve()
    expected = {"index.html", *(
        f"docs/{path.stem}.html" for path in (ROOT / "docs").glob("*.md")
    )}
    pages = {}
    for path in site.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(site).as_posix()
        if "{{" in text or "{%" in text:
            fail(f"{relative}: unresolved template syntax")
        pages[relative] = Page(text)
    if set(pages) != expected:
        fail(f"Generated pages differ: expected {sorted(expected)}, got {sorted(pages)}")
    if not exact_file(site, Path("sitemap.xml")):
        fail("Generated sitemap.xml is missing")
    count = 0
    for relative, page in pages.items():
        route = "/" if relative == "index.html" else f"/{relative}"
        page_url = f"{origin}{prefix}{route}"
        if page.h1_count != 1:
            fail(f"{relative}: expected one h1, got {page.h1_count}")
        if page.canonical != [page_url]:
            fail(f"{relative}: incorrect canonical URL: {page.canonical}")
        for target in page.links:
            url = urlsplit(urljoin(page_url, target))
            if url.scheme not in ("http", "https") or url.netloc != urlsplit(origin).netloc:
                continue
            count += 1
            path = unquote(url.path)
            if not path.startswith(prefix + "/"):
                fail(f"{relative}: link loses repository prefix: {target}")
                continue
            local = path[len(prefix) + 1:]
            if local.endswith("/") or not local:
                local += "index.html"
            if local.endswith(".md"):
                fail(f"{relative}: unconverted Markdown link: {target}")
            if not exact_file(site, Path(local)):
                fail(f"{relative}: missing generated path or wrong casing: {target}")
            elif url.fragment and local in pages:
                if unquote(url.fragment) not in pages[local].ids:
                    fail(f"{relative}: missing generated anchor: {target}")
    print(f"Generated-site check: {len(pages)} pages, {count} local URLs inspected.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, help="Jekyll output directory")
    args = parser.parse_args()
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    origin = scalar(config, "url").rstrip("/")
    prefix = scalar(config, "baseurl").rstrip("/")
    repository = scalar(config, "repository")
    owner, name = repository.split("/")
    if origin.lower() != f"https://{owner.lower()}.github.io" or prefix != f"/{name}":
        fail("url/baseurl do not match the configured project repository")
    check_sources()
    if args.site:
        check_site(args.site, origin, prefix)
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Documentation checks passed. External destinations were not fetched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
