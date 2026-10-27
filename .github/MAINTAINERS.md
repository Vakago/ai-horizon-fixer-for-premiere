# Copy this package into the public repository

Destination: [Vakago/ai-horizon-fixer-for-premiere](https://github.com/Vakago/ai-horizon-fixer-for-premiere).

1. Copy the **contents** of `public-docs/` to the public repository root. Include the hidden `.github/` folder and `.gitignore`. Do not create a `public-docs/` folder inside the destination. Use a local checkout or GitHub Desktop if a browser upload omits hidden files.
2. Review the files against the published package. The guides describe the current UXP interface; published version and platform support have not been independently verified. The older Horizon Fixer is linked separately.
3. Enable **Issues** in repository Settings. Bug report and Feature request forms are included. No custom labels are required.
4. Use `main` as the default branch, or update the push branch in `.github/workflows/pages.yml` if the repository uses a different name.
5. In **Settings > Pages > Build and deployment**, select **GitHub Actions** as the source. Allow Actions in the repository and permit the `github-pages` environment to deploy from the default branch.
6. When ready to publish, commit/upload the package and start **Documentation and GitHub Pages** from the Actions tab, or push to `main`. The workflow checks links, builds Jekyll, checks generated HTML and deploys only from the default branch. Pull requests build and check without deploying.
7. Check the completed workflow and visit [the documentation site](https://vakago.github.io/ai-horizon-fixer-for-premiere/). Open every navigation link and the issue chooser, test the download destination, and check a narrow viewport. Set the repository's About website to the documentation URL or official product page.

The prepared Pages address is `https://vakago.github.io/ai-horizon-fixer-for-premiere/`. `_config.yml` sets `url: https://vakago.github.io`, `baseurl: /ai-horizon-fixer-for-premiere` and the matching `repository`. If the repository is renamed or moved, update these values, GitHub links in the guides and issue-template contact links together. Configure a custom domain only when intentionally changing these URLs.

## Maintain the documentation

Keep ordinary links as relative Markdown `.md` links. They work when read on GitHub; `jekyll-relative-links` converts them to site paths at build time. The README has the site-root permalink. Layout links use `relative_url` to retain the repository prefix. Use lower-case documentation filenames and stable heading anchors.

The site uses GitHub's supported Cayman theme, a small shared layout, SEO metadata and a sitemap. Each guide has its own title and description. No custom domain, analytics, extension source, extension build system or binary downloads are included. The official product and download links remain prominent on each generated page.

Run the source check from the copied repository root:

```sh
python .github/scripts/check_docs.py
```

For a local site preview with Ruby and Bundler installed:

```sh
bundle install
bundle exec jekyll build
python .github/scripts/check_docs.py --site _site
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/ai-horizon-fixer-for-premiere/`. These commands build the documentation only. The Actions workflow uses GitHub's Jekyll builder, so no local Ruby setup is needed for deployment. See [GitHub's custom Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

Keep the extension proprietary. This package intentionally adds no open-source license or new product terms. Confirm any documentation licensing policy separately before adding a license. Do not copy private project files, internal evidence, media supplied by customers or extension binaries into this repository.

## Verification at export

On 27 October 2026, local checks passed for Markdown links and heading anchors, filename casing, repository URL configuration, YAML parsing, formatting and repository context budgets. The generated-HTML checker was exercised with temporary fixtures, including broken-prefix and missing-anchor cases.

Ruby/Jekyll and Docker were unavailable locally, so the actual Jekyll build and rendered desktop/mobile site have not been verified. The supplied workflow has not been run against the public repository. Its generated-site check must pass before deployment. Product and current Exchange destinations were supplied by the owner; their live contents, published release version and availability were not independently confirmed. No extension behavior, installed-host support or AI quality was newly tested during this documentation task.

[Documentation overview](../README.md)
