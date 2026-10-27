---
title: Settings, zoom and Adobe Motion controls
description: Understand AI Horizon Fixer defaults, frame sampling, smoothing, automatic crop, GPU processing and Rotation or Scale keyframes.
---

# Settings, zoom and Adobe Motion controls

## Defaults and saved settings

| Setting                      | Default                               | Practical effect                                     |
| ---------------------------- | ------------------------------------- | ---------------------------------------------------- |
| Add keyframe                 | Off in At playhead and Selected clips | Apply a constant correction across the clip          |
| Auto-fill edges              | On                                    | Request automatic Scale for a whole-clip correction  |
| Zoom for point keys and Auto | Constant                              | Use a steady automatic Scale                         |
| Framing                      | Preserve existing framing             | Keep the current framing as a starting floor         |
| Analyze every N frames       | 60                                    | Control the interval between Auto samples            |
| Smoothing                    | Medium                                | Moderate changes in the Auto correction curve        |
| Processing                   | GPU, with CPU fallback                | Use available acceleration or fall back to CPU       |
| Alignment guides             | Grid                                  | Provide a fixed visual reference for manual rotation |

Most preferences are saved when storage is available. Each new panel session starts with **Auto-fill edges on**, and **Advanced** and **Preview / Manual Rotation** collapsed. If you want to preserve Scale during a whole-clip edit, check Auto-fill again after reopening the panel. Zoom choices for Auto and the two point-correction modes are stored separately.

The **Reset extensions settings** button restores panel preferences only. It does not change clips. If preferences cannot be saved, the current session can still use them.

## Auto-fill for whole-clip corrections

Rotating an image can expose empty corners. **Auto-fill edges** requests enough Scale to cover the frame where the clip's geometry is supported. This zooms in and crops the edges. It does not generate new image content.

Turn Auto-fill off to leave Scale and its animation unchanged, then frame the clip yourself. In Advanced, Framing choices apply only when automatic Scale is enabled.

## Zoom for point keyframes and Auto

| Policy   | Scale behavior                                | Trade-off                                                |
| -------- | --------------------------------------------- | -------------------------------------------------------- |
| Off      | Preserve Scale and its animation              | Corners may need manual framing                          |
| Constant | Use one covering automatic Scale for the clip | A steady crop can be tighter than needed at some moments |
| Dynamic  | Change automatic Scale with the correction    | Crop can move or appear to breathe                       |

Constant and Dynamic can replace existing Scale animation after confirmation. Choose Off when preserving your Scale keys matters more than automatic coverage.

Automatic keyframe framing requires supported centered, uniform geometry. Turn off Premiere's **Scale to Frame Size** for these modes. Readable Motion Scale from Fit/Fill framing is supported where the geometry can be verified. If automatic framing is unavailable, choose Off and adjust Scale manually.

## Preserve existing framing or Minimum fill

**Preserve existing framing** retains your current framing as a floor and adds Scale when coverage requires it. Start here when you already like the composition.

**Minimum fill** seeks the smallest supported Scale that covers the rotated frame, so it may reduce an existing crop. It has stricter geometry requirements; whole-clip Minimum fill requires matching source and sequence dimensions and pixel aspect ratio. If it is unavailable, use Preserve existing framing or disable automatic Scale.

Neither policy guarantees edge coverage for arbitrary transforms, effects, transparent borders or unusual media. Always check the Program Monitor across the full shot.

## Sampling and smoothing

**Analyze every N frames** accepts a positive whole number. A smaller interval analyzes more images and can catch changes between wider samples, at greater processing cost. The first and last included frames are sampled too.

An interval of **60 frames** corresponds to 2 seconds at 30 fps and 1 second at 60 fps. It is a frame interval, not a fixed duration setting.

**Smoothing** offers Off, Low, Medium and High. Higher smoothing reduces small variations but can soften fast or intentional changes. Compare the full shot at playback speed. Neither more samples nor stronger smoothing guarantees a better estimate.

## Processing and local analysis

The default requests GPU processing and falls back to CPU when needed. You can select **CPU** in Advanced processing settings. GPU availability depends on the system and host environment; processing speed and numerical results can differ between backends.

AI frame analysis runs locally using the included model. Footage is not uploaded to a cloud AI analysis service. Adobe installation, account and operating-system services have their own requirements. This local-analysis description is not a claim about every service on your computer.

## Inspect the edit in Adobe Premiere

Open **Window > Effect Controls**, select the clip and expand **Motion**:

- **Rotation** is the clip angle. AI or manual correction writes this property, either as a constant value or with keys.
- **Scale** changes image size. Increasing it can hide rotated corners while cropping more image.
- **Position** and **Anchor Point** affect composition and the center of rotation. Unusual or animated transforms can make automatic framing unavailable.

See Adobe's [Motion effect guide](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/apply-motion-effect.html). Check existing keys before accepting replacement warnings. Point corrections preserve other Rotation keys, but that does not mean an automatic Scale operation preserves Scale keys.

## Reset rotation and scale versus Undo

**Reset rotation & scale** sets Motion Rotation to **0°** and Scale to **100%**, removing **all keyframes on both properties**, including ones created outside this extension. It asks for confirmation. In Selected clips, select just one clip to use Reset.

Reset does not restore the state from before an AI correction and does not necessarily fit the source to the sequence. Use Premiere's **Undo** to reverse an applied edit. A batch has a separate Undo step for each corrected clip.

Resetting panel preferences changes settings only. It is separate from this timeline Reset action.

[Documentation overview](../README.md) · [Workflows](workflows.md) · [Compatibility](compatibility.md) · [Troubleshooting](support.md)
