# Color, attention and readable preparation

Verified local reference study,21October2026. This pass adds20seconds of consecutive-frame viewing and a tested manual-region audit. No Adobe project or existing color job was changed. The observations do not establish full AV flow, lyric timing or the original creators' software.

## What was actually inspected

| Reference | Scope | Observed structure |
|---|---|---|
| Know My Name `mlFxxNsExJc` |16–26s,24fps,240frames | Glasses/eyes; graphic light bridge; leaning figure; wide room; foreground group; bowed face/hands; another light-assisted change |
| STAR WALKIN' `HYsz1hP0BFo` |64–74s,24fps,240frames | City/trophy graphic; isolated trophy; face; ring/hand; boot; medium character; new group/environment |

All ten consecutive pages, two adjacent-change boards and five detail pages were viewed.33source-resolution details were extracted and inspected as aspect-preserving resized panels. One additional STAR WALKIN' glasses frame was viewed individually. These are local sample-based visual inspections, not listening.

STAR WALKIN' has clear face entry at66.000, hand detail at67.750, boot at70.583333, medium character at72.458333 and new environment at73.916667. The hand shot lasts2.833333s, boot1.875s, medium1.458333s before the next cut. Face-to-hand preparation does not need a new effect on every beat. A white flash at64.666667 and the isolated trophy view at64.750 are separate events; do not count the flash as a new camera shot by itself.

Know My Name's ordinary scene/angle entries were checked at17.666667,19.875,22.125 and24.166667. The complete intervals between those are2.208333,2.250 and2.041667s. There is a separate stylized bridge beginning16.583333. Around24.958333 the head/body size changes while the pose develops, followed by an orange/white bridge and a bespectacled hooded view at25.125. Do not promote24.958333 to a confirmed cut merely because a scene detector or size change fires; the underlying boundary/identity continuity remains uncertain.

## Energy is not visual density

The cached Know My Name16–24s average RMS was relatively low within that file, yet16.5–17.7s contains strong reflection, streak and light events. Later shots in the same window hold for about two seconds. An eight-second average cannot decide which individual frames should be quiet. It is also not a loudness-normalized comparison between songs.

Use audio measurements to shortlist passages, then inspect local visuals and actual attacks. In the STAR WALKIN' hand entry, nearest low-band candidate was131.33ms later while the snare-like candidate was8.67ms earlier. At boot entry, the nearest low-band candidate was about248ms later. This does not prove a snare-driven edit or a missed beat: the full mix, detector windows/thresholds and hearing remain unverified. It does refute treating every selected cut as numerically justified by the nearest bass peak.

Know My Name's cached ASR has no segment overlapping16–26s; absence is not instrumental proof. STAR WALKIN' has draft words over the passage, but no audible word alignment was verified. An expression→hand→foot sequence can be described as preparation without inventing a particular lyric motive.

## Separate a local highlight from a global mismatch

In STAR WALKIN'66.083333→66.166667, an explicitly marked glasses patch changed about+140.55/255 in a weighted **encoded RGB brightness proxy**. A nearby cheek patch changed+0.90, a leaves patch−0.046, and the whole selected picture area+4.48. The return frame66.333333 was also inspected. The white reflection is visibly localized; matching the whole frame to remove its global statistic would disturb regions that hardly changed.

These values are image-code proxies, not linear luminance, stops, IRE, measured skin accuracy or calibrated color. They come from a stylized animation reference. They do not validate a skin grade for real footage. The visible lighting/reflection relationship is observed; the split between original lighting, animation and grading is unknown.

For live-action footage, normalize capture transfer/exposure/white balance on suitable stable footage, then match neighboring shots in context. Preserve a motivated short highlight or venue-colored light instead of forcing every frame to the same mean RGB. Compare subject and background separately. A bright equipment screen or blue trampoline floor can dominate a global statistic without the child's face needing the same correction. Check HDR/tone mapping and actual native exports separately.

In Premiere, use the native original-linked clips and inspect stable pre/post-accent frames with scopes/Comparison View before adjusting Lumetri. An authorized isolated graphic glint belongs on a separate AE/effect layer when that better preserves the underlying plate. This is an implementation proposal, not a native color/render test performed in this pass. Do not intervene in another editor's color work while researching.

## Attention is editorial annotation, not gaze tracking

The study manually marked nine approximate story anchors. Hand→boot moved0.151 in normalized picture coordinates; boot→medium face0.260. Know My Name wide-room→foreground-group moved0.412, then group→bowed detail0.433. Those are distances between the chosen markers, not eye-tracking results or quality scores. Large jumps can deliberately establish another person/part of the space. Decide whether the intended subject is readable before adding a transition to hide a reset.

Transfer the sequence's function: recognisable child/activity→hand on control or VR adjustment→foot preparing on trampoline→readable action/reaction. Retain enough time to understand each activity. Do not borrow the reference's sombre expression or add a false action/result. A cropped frame must still preserve the action origin, destination and relevant faces; normalized coordinates alone cannot approve a9:16 crop.

## Portable region audit

Run `python scripts/region_continuity.py PLAN.json --output NEW_FOLDER` using [the portable helper](../scripts/region_continuity.py). It needs Pillow, reads original images, refuses an existing output folder, writes numeric JSON and annotated boards. It does not touch Adobe, grade footage or detect faces/skin/gaze. Review the overlay before marking annotations verified.

Minimal plan schema; replace every example with inspected real files/coordinates:

```json
{
  "frames": [{
    "id": "before", "image": "frame-before.png",
    "analysis_box": [0, 0.125, 1, 0.875],
    "focus": [0.57, 0.51], "focus_label": "manual glasses anchor",
    "regions": [{"name": "highlight", "rect": [0.59, 0.44, 0.68, 0.59]}]
  }, {
    "id": "during", "image": "frame-during.png",
    "analysis_box": [0, 0.125, 1, 0.875],
    "focus": [0.57, 0.51],
    "regions": [{"name": "highlight", "rect": [0.59, 0.44, 0.68, 0.59]}]
  }],
  "transitions": [{"from": "before", "to": "during", "reason": "local reflection"}]
}
```

Rectangles/points are normalized **inside** `analysis_box`; do not mix full-canvas and cropped coordinates. The example box is only an inner-picture crop used for these letterboxed references, not a universal film gate. Images may use different profiles; the helper records embedded ICC presence but does not apply it. Its means cannot replace managed-color comparison or HDR/SDR verification. Same-named rectangles are not automatic physical tracking, so movement/occlusion can invalidate them.

The helper was run on nine real extracted frames/seven comparisons; the annotated boards were inspected. Invalid/out-of-bounds ROI, duplicate frame ID, missing source and existing output were rejected without overwriting outputs; source PNG hashes stayed unchanged.

Local provenance: `analysis/attention_pass8`, the two `Sequence_16.000_10.000_stride1` and `Sequence_64.000_10.000_stride1` folders, plus the pass8 checkpoint. For a larger action/narrative treatment, combine these findings with the [narrative study](narrative-continuity-study.md); for graphic cadence use the separate [brush study](brush-language-study.md).
