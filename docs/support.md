---
title: Troubleshooting, bug reports and feature requests
description: Fix common AI Horizon Fixer installation, preview, rotation and crop problems, or report a Premiere extension issue through GitHub.
---

# Troubleshooting, bug reports and feature requests

## Installation or missing panel

Check that the correct AI Horizon Fixer edition is installed and enabled in Creative Cloud **Manage Plugins**. The current UXP panel is under **Window > UXP Plugins > AI Horizon Fixer**. Restart Premiere after installation if needed. See [installation](getting-started.md) and [legacy differences](compatibility.md#current-and-legacy-horizon-fixer).

If Creative Cloud reports an installation error, record its exact text and use Adobe's [plugin installation guidance](https://developer.adobe.com/premiere-pro/uxp/plugins/distribution/install/). Account or purchase questions belong with [Vakago Tools support](https://vakago-tools.com/contact/).

## No clip found or an action is unavailable

Open an active sequence and move inside an enabled video clip for **At playhead**. In **Selected clips**, check that the timeline selection contains video. For **Auto**, select exactly one supported video. Relink offline media and check that the target is editable.

Manual preview and Reset need one selected video in Selected clips. Multiple selection is for AI batch processing. Read any explanation shown by the panel before changing the sequence.

## Preview or AI processing does not start

Wait for frame capture, then use **Refresh preview** or **Retry frame** when offered. Confirm the displayed frame belongs to the target. Try **CPU** in Advanced processing if the GPU route is unavailable or unreliable. Manual rotation does not run AI, but still needs a usable frame preview.

If the panel reports a startup timeout, retry once and record the message if it repeats. Updating the Creative Cloud desktop app and refreshing Adobe sign-in resolved one reported startup problem, but this is not a universal fix. Save your work before restarting applications. Do not assume every timeout is a licensing fault.

## Wrong angle, empty corners or unexpected crop

| Symptom                                          | What to check                                                                                             |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| AI angle looks wrong                             | Use [Manual Rotation](workflows.md#rotate-manually), and consider whether the camera tilt was intentional |
| Visible layers affect the estimate               | Temporarily simplify overlapping videos, graphics or adjustment layers around the target                  |
| Empty corners after rotation                     | Check Auto-fill or Zoom; adjust Motion Scale manually if automatic framing is unavailable                 |
| Too much crop                                    | Compare Preserve existing framing with supported Minimum fill, or use Zoom Off and frame manually         |
| Crop changes over time                           | Dynamic zoom changes Scale; consider Constant for a steady crop                                           |
| Automatic keyframe zoom is unavailable           | Check supported centered uniform geometry and turn off Scale to Frame Size, or choose Zoom Off            |
| Manual preview looks different from final output | Judge the result in Program Monitor; the preview is a captured still and can already include crop         |

See [settings and Motion controls](settings.md) before replacing existing Scale or Rotation animation.

## Partial batches, skipped samples and cancellation

Open **Clip details** after a batch and review completed, skipped and failed clips. Cancelling does not roll back edits already applied. Undo once for each corrected clip if you want to reverse those changes.

After Auto, inspect reported skipped times and use **Retry skipped samples** when available. An applied curve may interpolate through a time whose analysis failed. Review those moments in Premiere. Read the outcome before rerunning, since another Auto pass can replace manual repairs or existing animation.

## Frequently asked questions

### Does AI analysis upload my footage?

AI frame analysis runs locally. It does not upload footage to a cloud inference service. Adobe installation and account services have separate requirements. See [processing](settings.md#processing-and-local-analysis).

### Does Reset undo the AI edit?

No. **Reset rotation & scale** sets Rotation to 0° and Scale to 100% and deletes their keys. Use Premiere Undo to reverse an applied edit. [Read the Reset details](settings.md#reset-rotation-and-scale-versus-undo) before confirming.

### Why did Auto-fill turn on again?

New panel sessions start with Auto-fill enabled. Check it before a whole-clip correction if you want Scale preserved. Other zoom choices and valid preferences can persist independently.

### Why are my controls different?

Check your extension version and whether you installed the current UXP edition or legacy Horizon Fixer. These guides do not establish feature parity between releases. See [compatibility](compatibility.md).

## Report a bug

Search [existing issues](https://github.com/Vakago/ai-horizon-fixer-for-premiere/issues), then choose **Bug report** from [New issue](https://github.com/Vakago/ai-horizon-fixer-for-premiere/issues/new/choose). Include:

- Extension version, current or legacy edition, Premiere version and operating-system version.
- Processor architecture, such as Intel, AMD or Apple Silicon, and GPU or CPU processing choice when relevant.
- Mode, Add keyframe, Auto-fill or Zoom, Framing, and Auto interval or smoothing where applicable.
- Steps to reproduce, expected result, actual result and the exact panel message.
- Relevant clip details, such as resolution, frame rate, trimming, speed changes, overlays and existing Motion keys.

Attach a screenshot or a small non-confidential example when useful. GitHub Issues are public. Remove personal data, license keys and private media. Use [private support](https://vakago-tools.com/contact/) for sensitive material or purchase details. If the outcome is uncertain, describe what is visible in Premiere before repeating an operation.

## Request a feature

Search existing requests, then choose **Feature request** from [New issue](https://github.com/Vakago/ai-horizon-fixer-for-premiere/issues/new/choose). Explain your editing goal, the current workaround and how the change would help. A concrete example is more useful than a control name alone. Requests do not imply a delivery commitment.

[Documentation overview](../README.md) · [Official product page](https://vakago-tools.com/ai-horizon-fixer/) · [Vakago Tools](https://vakago-tools.com/)
