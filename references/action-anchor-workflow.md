# Action anchors and native audio alignment

Verified local study, 21 October 2026. This is a five-second technical/visual experiment, not a final JUMP design or a listening-approved edit. It demonstrates three original-linked activities, distinct cut/action timing, short outgoing blur, a small native impact mark and a measured audio correction. Reference-film pixel assets were not used.

## Keep four time domains explicit

1. Original camera PTS and capture rate.
2. Native source-time mapping after retiming.
3. Integer delivery frame and composition rate.
4. Intended decoded music source time, plus any independently measured native import/output delay.

For a constant-speed segment: `source_in = action_source_time - speed * (action_delivery_frame - shot_in_frame) / delivery_fps`. With changing speed, keep explicit source-time anchors and interpolate each segment. Audit the source-time property after creating the native project; a JSON plan alone does not prove the project matches it.

Quantize each intended event from absolute time: `frame = round((music_event - music_start) * fps)`. Do not repeatedly add rounded frames-per-beat. Cut entry and action payoff are independent decisions. An incoming shot can begin on one attack, show preparation, then strike on a later attack.

## Tested plan and uncertainty

Main composition: 1080×1920, 30 fps, 150 frames. Intended JUMP source excerpt begins at 32.921330 s. Numeric candidates came from the low/high percussive analysis, not listening.

| Event | Delivery frame | Music candidate source s | Quantized offset ms |
|---|---:|---:|---:|
| Tan arcade ball separates from hand | 22 | 33.64133 | +13.333 |
| Cut to boxing preparation | 37 | 34.16133 | -6.667 |
| Blurred fist/bag overlap and deflection | 62 | 34.99133 | -3.333 |
| Cut to trampoline | 87 | 35.82133 | 0 |
| Tucked airborne pose | 96 | 36.13133 | -10 |
| Knees compress / seated transition | 121 | 36.96133 | -6.667 |

These are frame-rounding offsets to analysis candidates. They are not measured perceptual sync errors. The boxing event has approximately 2.4024–2.435767 s source uncertainty because of motion blur. The compression interval is approximately 5.005–5.088417 s. It is **not** first foot-to-mat contact. The tucked pose is not proof of the absolute jump apex. A second purple ball belongs to another throw; track the selected tan ball before labeling its release.

Anonymous clips G097/G105/G124 came from privately supplied indoor games footage; the originals are not included. G110 was rejected after viewing 21–25.5 s: the selected child was already slow/stationary near the slide bottom, so a previous 23.5 s label did not establish an arrival impact. Do not inherit action labels from an old edit plan without inspection.

## Retime and framing revision

At 60000/1001 capture to 30 fps delivery, sampling-floor speed is `30/(60000/1001) = 0.5005`. The boxing preparation uses that speed, then returns to 1× at the contact anchor. No Optical Flow was used. Trampoline segments are 1.2×, 0.5005×, approximately 0.9593× and 0.8×. These are deliberately piecewise-linear source-time segments, not a claim of a continuously eased speed ramp.

The first render revealed a clipped face at boxing entry and a hand close to the top at trampoline entry. Corrected boxing to exact source fit (62.5% native scale), selected later preparation while preserving frame-62 impact through slow playback, and reduced trampoline crop from 125% to 110% native scale. Reinspect entry, payoff **and** recovery; checking only the hero pose misses crop failures.

A whole-study overview then exposed an additional error: reducing scale while retaining position x=0 left the source right edge at x=950.4 on a 1080-wide canvas. The dark trampoline made that strip easy to miss in small event sheets. The subject also left the frame during late recovery. A third native pass moved the plate to x=150, then followed the child from `[150,1340]` at frame121 toward `[420,1050]` at frame149. The final native audit checks transformed source bounds on **every** delivery frame.

For an unrotated, unparented 2D layer with centred anchor, coverage requires `position_x - source_width * scale_x / 200 <= 0` and `position_x + source_width * scale_x / 200 >= comp_width`, plus the equivalent vertical inequalities. Different anchors, rotation, parents, masks and lens effects need their actual transformed corners. Comparing styled versus clean renders cannot catch a crop error shared by both. Mathematical coverage cannot prove a readable face/body; view the full recovery too.

Outgoing blur occupies the final two frames; the incoming frame is sharp. In the corrected export, settled styled/clean frame mean RGB differences were about 0.94–1.86/255, consistent with compression differences away from the added accent/transition. Actual boards were also viewed; a low mean error does not prove good composition by itself.

## Measure the exported audio

The first native render correlated to the intended decoded source excerpt at 0.99389 but lagged **21.333 ms**. This passed a loose one-frame bound yet remained a correctable offset. In the next new AEP, the native music in-point was advanced by that measured amount to 32.942663333 s. The intended excerpt start remained 32.921330 s in the plan. Remeasurement returned 0 ms lag at 24 kHz analysis resolution and correlation 0.999674.

This result is local to the tested media/native path. Do not assume all AAC files or Adobe exports need the same shift. Preserve both values and the reason for the correction. Use normalized cross-correlation over a non-silent several-second excerpt; compare gain, stereo/channel handling and residual, and limit lag search around the expected position. Periodic drums can create ambiguous peaks; a strong correlation is not musical listening approval.

The study intentionally reduced music by 6 dB. Final measured input loudness of the rendered MP4 was -12.39 LUFS, true peak -5.72 dBTP. The `loudnorm` **output** estimate printed by a null measurement pass is not a normalization already applied to the file. Preserve user gain on real work unless a change is authorized.

Both MP4s fully decoded: 30 fps, 150 frames, AAC 48 kHz stereo. The independent original impact mark decoded as ProRes 4444 with alpha, 400×400, 120 fps, 20 frames, no audio. Its animation samples are generated graphics; they do not increase the camera footage's captured motion detail. It is a short mark without extra blank render handles.

## Reusable plan check

Run `python scripts/check_action_anchors.py PLAN.json`. The script reads only and prints JSON. It checks continuous shot coverage, ordered source-time keys, declared action mappings and speeds against the recorded capture rate. A below-floor segment is a review warning, since an intentional freeze may be valid. It does not probe VFR, verify source identity, render a native project, classify contact, or listen.

Minimal schema example (all paths/times must be replaced for the actual job):

```json
{
  "delivery_fps": 30, "duration_frames": 60,
  "music": {"source_start_s": 10},
  "shots": [{"id": "shot-01", "in_frame": 0, "out_frame_exclusive": 60,
    "capture_fps": 59.94005994,
    "source_time_keys": [{"delivery_frame": 0, "source_s": 2}, {"delivery_frame": 60, "source_s": 4}]}],
  "events": [{"label": "inspected release", "delivery_frame": 30,
    "source_id": "shot-01", "source_target_s": 3, "music_source_candidate_s": 11}]
}
```

Prompt for the next editor: “Inspect the preparation, event interval and recovery. Keep shot entry and in-shot action anchors separate. Preserve integer delivery frames, original camera paths and explicit source-time keys. Measure actual exported music offset before claiming sync. Show source/event/cut evidence and label any unverified audible or lyrical interpretation.”

## Verified native scripting correction

`AVLayer.frameBlending` is read-only on the tested AE 26.5. Writing it caused the first isolated build to fail before saving an AEP. Use `layer.frameBlendingType = FrameBlendingType.NO_FRAME_BLEND` when disabling interpolation. The corrected project rendered successfully. Preserve failed-attempt diagnostics; do not retry against a populated live project.

Evidence lives in the project's `native_study_03` (first render), `native_study_03_rev2` (audio/entry revision), `native_study_03_rev3` (final framing/coverage revision), `scripts/build_native_sync_study.jsx`, and `notes/Pass4_2026-10-21.md`. An installed portable skill should rely on this method rather than assuming those project folders exist on another machine.
