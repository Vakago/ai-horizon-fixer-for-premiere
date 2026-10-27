---
title: Install AI Horizon Fixer and straighten your first clip
description: Install the Premiere UXP extension through Adobe Exchange, find its panel and make a whole-clip horizon correction.
---

# Install AI Horizon Fixer and straighten your first clip

## Check the requirements

The current UXP extension requires **Premiere Pro 25.6.5 or later** and the Creative Cloud desktop app for installation. Check the [Adobe Exchange listing](https://exchange.adobe.com/apps/cc/d4a30c97/vakago-ai-horizon-fixer-for-premiere) for operating-system support, availability and purchase details. Earlier Horizon Fixer releases have different requirements and controls; see [compatibility](compatibility.md).

## Install and open the panel

1. Open [AI Horizon Fixer on Adobe Exchange](https://exchange.adobe.com/apps/cc/d4a30c97/vakago-ai-horizon-fixer-for-premiere) and follow the installation instructions for your Adobe account.
2. Complete installation in the Creative Cloud desktop app. If browsing there directly, look under **Stock & Marketplace > Plugins**. Confirm that AI Horizon Fixer is installed and enabled in **Manage Plugins**.
3. Open or restart Premiere, then choose **Window > UXP Plugins > AI Horizon Fixer**.
4. Open your project and an active sequence containing a video clip.

If Vakago Tools supplies a `.ccx` installer directly, double-click it and follow Creative Cloud's installation prompts. The GitHub repository contains documentation, not an installer. Adobe describes both installation methods in its [Premiere UXP installation guide](https://developer.adobe.com/premiere-pro/uxp/plugins/distribution/install/).

## Make a first correction

Start with an ordinary video clip where the tilt stays fairly steady. Keep a copy of your sequence when exploring unfamiliar controls.

1. Place the playhead inside the clip, on a frame with useful alignment cues.
2. Choose **At playhead**. This targets the video at that position independently of the timeline selection.
3. Leave **Add keyframe** unchecked. The correction will be constant across the clip, based on this one frame.
4. Keep **Auto-fill edges** on initially. It adjusts Scale to cover corners exposed by rotation, which crops some of the image.
5. Click **Straighten with AI**. Read any warning about replacing existing Rotation or Scale animation before confirming.
6. Check the Program Monitor and play through the shot. Use Premiere's **Undo** if you want to reverse the applied edit.

If the angle needs a small adjustment, use [Preview / Manual Rotation](workflows.md#rotate-manually). If the tilt changes during the shot, use [point keyframes or Auto](workflows.md).

## Know what to review

Look at the horizon, subject composition and image edges. AI can misread a scene or remove an intentional camera tilt. A single-frame estimate does not follow motion throughout the shot. Rotation correction does not remove camera shake or repair perspective.

Open **Window > Effect Controls**, then expand **Motion** to inspect **Rotation** and **Scale**. See [settings and Adobe Motion controls](settings.md#inspect-the-edit-in-adobe-premiere) for how these interact.

If no target appears or the panel will not open, follow [troubleshooting](support.md).

[Documentation overview](../README.md) · [Official product page](https://vakago-tools.com/ai-horizon-fixer/)
