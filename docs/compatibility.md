---
title: Compatibility, older versions and limitations
description: Check Premiere requirements, distinguish current AI Horizon Fixer from legacy Horizon Fixer and understand supported timeline workflows.
---

# Compatibility, older versions and limitations

## Premiere and operating systems

The current AI Horizon Fixer UXP extension requires **Premiere Pro 25.6.5 or later**. This is the minimum requirement, not a guarantee that every later Premiere version, operating system or processor has been tested.

Check the [current Adobe Exchange listing](https://exchange.adobe.com/apps/cc/d4a30c97/vakago-ai-horizon-fixer-for-premiere) for the operating systems and host versions supported by the package you install. A complete verified Windows, macOS, Intel and Apple Silicon support matrix is not established by this documentation. In particular, successful standalone runtime tests on a processor do not establish installed Premiere support.

GPU processing is system-dependent. CPU is available as a processing option and fallback. Do not assume identical speed or results across GPU, CPU or different computers.

## Current and legacy Horizon Fixer

| Edition                                | Product and installation                                                                                                                                                             | How to identify it                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Current AI Horizon Fixer               | [Official product page](https://vakago-tools.com/ai-horizon-fixer/) and [current Exchange listing](https://exchange.adobe.com/apps/cc/d4a30c97/vakago-ai-horizon-fixer-for-premiere) | UXP panel with At playhead, Auto and Selected clips in the current interface |
| Legacy Horizon Fixer (Straighten Tool) | [Legacy product page](https://vakago-tools.com/horizon-fixer-extension/) and [legacy Exchange listing](https://exchange.adobe.com/apps/cc/108734/horizon-fixer-straighten-tool)      | Earlier extension with a different interface and horizon-line workflow       |

The current UXP panel opens under **Window > UXP Plugins**. Earlier CEP extensions use Premiere's **Extensions** menu. Use the instructions and compatibility requirements for your installed edition.

This guide covers the current UXP controls. It does not promise AI, Auto, settings, platform support or workflow parity with the legacy extension. It also does not establish purchase entitlement or automatic migration between listings. Ask [Vakago Tools](https://vakago-tools.com/contact/) about purchase or upgrade questions.

This guide references the UXP interface identified as version **1.0.1**. That does not establish which version is currently published on Exchange. If your installed version differs, include it in support reports and use the listing's release information.

## Footage and timeline limitations

Start with ordinary forward, constant-speed video clips. Relink offline media and use an editable target. Animated correction does not support nested, multicam or merged clips, reversed footage or speed changes in the current supported workflow.

The target must be the only visible video clip at the frame to analyze. Hide overlapping videos, graphics and adjustment layers. Auto requires the target to be the only visible video throughout its trim. The captured sequence still can include the target's applied effects and existing crop.

General support is not established for transitions, proxies, speed remapping, arbitrary Position or Anchor Point changes, nonuniform transforms, extra crops or effects, orientation metadata, fisheye or anamorphic footage, and transparent borders. Automatic Scale has additional [geometry requirements](settings.md#zoom-for-point-keyframes-and-auto).

Manual preview shows a captured still and may already be cropped. It is an alignment aid, not a complete simulation of the final framing.

## AI estimates and published versions

AI can mistake scene geometry or an intentional camera roll. Review the horizon, motion and crop in Premiere. Horizon correction rotates and frames video; it does not stabilize camera shake, correct perspective or generate missing edges.

The guides describe current controls and documented behavior. Availability of Auto, smoothing or zoom options in a build does not itself establish completed quality testing or acceptance on every installed host. If the published package differs, report its version and the missing or changed control rather than assuming it has the same capabilities.

[Documentation overview](../README.md) · [Installation](getting-started.md) · [Troubleshooting and support](support.md)
