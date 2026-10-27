---
title: Horizon correction workflows
description: Choose whole-clip AI correction, selected clips, point keyframes, Auto sampling or manual rotation in AI Horizon Fixer.
---

# Horizon correction workflows

These instructions cover the current UXP interface. Compare your installed version with [compatibility and older releases](compatibility.md) if the controls differ.

## Choose the target and correction type

| Mode           | Target                                 | Frame analyzed                                  |
| -------------- | -------------------------------------- | ----------------------------------------------- |
| At playhead    | Video at the current playhead position | Current frame                                   |
| Selected clips | Selected timeline videos               | Each clip's first included frame after trimming |
| Auto           | Exactly one selected video clip        | Samples throughout the trimmed clip             |

In At playhead and Selected clips, **Add keyframe** switches between one whole-clip correction and a correction at a specific time. Auto creates a correction curve across the clip.

## Correct a whole clip

Use a whole-clip correction for a shot with a steady tilt. In **At playhead**, choose a representative frame, leave **Add keyframe** off and click **Straighten with AI**. The chosen angle applies across the clip, rather than tracking each frame.

Leave **Auto-fill edges** on to request automatic Scale, or turn it off to preserve Scale and frame the result yourself. Read any animation replacement confirmation. Existing Rotation animation can be replaced by the constant correction.

## Correct selected clips

1. Select the video clips in your timeline and open **Selected clips**.
2. Check the selection count. Linked audio is not analyzed.
3. Leave **Add keyframe** off for constant corrections, or enable it to correct each clip at its first included frame.
4. Click **Straighten with AI** or **Apply AI keyframe**, according to that choice.
5. Expand **Clip details** to inspect each result and any skipped or failed clips.

Keep the selection unchanged while processing. Clips are processed one at a time. **Cancel** stops pending work; edits already applied remain. Each corrected clip has its own Premiere Undo step, so inspect the report before repeating a batch.

Selected clips does not analyze every frame of every selected video. Use Auto on one clip at a time for a changing horizon.

## Add or update a point keyframe

1. In **At playhead**, move to the time you want to correct.
2. Enable **Add keyframe** and choose a [Zoom policy](settings.md#zoom-for-point-keyframes-and-auto).
3. Click **Apply AI keyframe**.
4. Move to another time and repeat where the angle needs to change.

The operation adds a Rotation keyframe or updates the key at that time. Other Rotation keys are preserved. New keys use Linear interpolation. With only one key, the correction holds across the clip; with multiple keys, review the movement between them.

In **Selected clips**, point keys go at each clip's first included frame. Switch to **At playhead** to correct a later moment. Zoom Off preserves Scale and its animation. Constant and Dynamic zoom can replace Scale animation after confirmation, even though other Rotation keys are preserved.

## Auto keyframes for a changing horizon

1. Select exactly one supported video clip and choose **Auto**. Verify the target.
2. Set **Analyze every N frames**. Start with the default **60**. Lower intervals analyze more frames and take longer. The first and last included frames are also sampled.
3. Start with **Medium** smoothing, then adjust based on the shot. Higher smoothing can soften rapid or intentional motion.
4. Choose **Constant** zoom for a steady crop, **Dynamic** for changing Scale, or **Off** to preserve Scale. See [zoom and framing](settings.md).
5. Click **AI auto-keyframe** and read any replacement confirmation. Auto applies after analysis; there is no separate approval of a results preview.
6. Play through the full clip. Check the horizon, movement between samples and crop.

Auto replaces Rotation animation on the clip. Constant or Dynamic zoom can also replace Scale animation. A later Auto run can replace manual repairs, so review its confirmation before rerunning.

If some samples fail, a result can still be applied using the successful samples. The curve bridges skipped times; those frames were not successfully analyzed. Inspect the report, review those moments yourself and use **Retry skipped samples** when offered. After cancellation, read the reported outcome before starting again.

To repair a moment after Auto, move the playhead there, switch to **At playhead**, enable **Add keyframe**, expand **Preview / Manual Rotation**, adjust the draft and click **Apply key**. Use Premiere Undo to reverse the applied operation. Sampling and smoothing are aids rather than a guarantee of correct motion.

## Rotate manually

Manual rotation is useful when AI chooses the wrong angle or when you want an intentional composition. It does not require AI analysis.

1. Expand **Preview / Manual Rotation**. In Selected clips, select only one video for manual preview.
2. Drag the image around its center to rotate the draft. Hold **Shift** for finer adjustment.
3. Choose **Grid**, **Line** or **Guides off** as your fixed reference.
4. Click **Apply**, or **Apply key** when Add keyframe is enabled. **Cancel** discards the draft.

For keyboard adjustment, focus the preview. **Left** or **Up** rotates counterclockwise; **Right** or **Down** rotates clockwise. Each step is **0.1°**, or **0.01°** with Shift.

Dragging changes only the draft. Applying changes the timeline. The preview is a captured still and may already include cropping or visible layers. Use the Program Monitor to judge the final framing.

## Practical starting points

| Shot                                     | Starting approach                                        | Review                                   |
| ---------------------------------------- | -------------------------------------------------------- | ---------------------------------------- |
| A landscape with a steady tilt           | Whole-clip AI with Auto-fill on                          | Horizon and crop across the shot         |
| A short shot that changes angle twice    | Point keyframes at useful moments                        | Movement between keys                    |
| A longer shot with changing roll         | Auto, 60-frame interval, Medium smoothing, Constant zoom | Missed changes, skipped samples and crop |
| A scene with few reliable alignment cues | Manual rotation with Line or Grid                        | Intended composition                     |
| A shot with carefully animated Scale     | Zoom Off, or Auto-fill off for a whole-clip edit         | Exposed corners and existing Scale keys  |

These are starting choices, not camera-specific presets or quality guarantees. See [limitations](compatibility.md#footage-and-timeline-limitations) for complex clips.

[Documentation overview](../README.md) · [Settings and Motion controls](settings.md) · [Troubleshooting](support.md)
