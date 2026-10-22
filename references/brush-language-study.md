# Drawing cadence, color roles and an original brush study

Verified visual/reference and native-tool study, 21 October 2026. Two new three-second reference passages were inspected at every source frame, then used to design a separate original AE asset. The reference authors' projects and software are unknown. The study is not full audiovisual or lyric verification.

## Observed reference evidence

| Reference | Scope | Visible events |
|---|---|---|
| GIVE THEM NOTHING / Veto `2FLY-gn-hGQ` | 38–41s, 24fps, 72 consecutive frames | Warm dimensional scene through38.166667; black field with cyan/cream drawing at38.208333. Similar paired rasters at38.291667/38.333333, then enlarged form at38.375. Cream tapered form develops a large opening by39.708333, expands by39.875, then curls/extends through40.458333 |
| VOCÊ É BRABA / Game Changers `69sKYwsxUM8` | 72–75s, 30fps, 90 consecutive frames | Held diagonal smear at72.000/72.033333; new smear direction at72.066667. Blue/white graphic at72.300; pink fragmentation at72.400; back-view action at72.766667. New angle at73.966667, face detail at74.100, extreme eye at74.400, wider reaction at74.500, portrait at74.733333 |

All four consecutive-frame pages were viewed. Twenty full-resolution details were extracted and inspected as640px contact-sheet cells; two details were also viewed individually. Veto's39.875 detail visibly includes fine hatching, large dark openings and a dot-like screen texture. Game Changers'74.400 eye has flat color regions, a slightly irregular contour and a character-shaped dark centre. These are visible raster properties. A black area in an opaque reference MP4 does **not** prove a transparent source layer or a particular mask/compositing technique.

Near-repeated pairs support deliberately held drawings in these passages. Veto's38.208333/38.250 image pair differed by about0.006/255 mean RGB in the320px sample;38.291667/38.333333 by0.366. Game Changers'72.000/72.033333 pair differed by0.114. Later samples have both two- and three-frame holds. Compression, source conversion and camera motion can affect such measurements. Do not infer an original12fps project or label every drawing change a camera cut.

## Interpretation and transfer

Possible reading: Veto's dark negative space and evolving drawn contours carry the direction from the preceding action; the Game Changers smear/fragmentation changes the scale and tempo before a readable new action. These are interpretations from images. Alternatives include a self-contained graphic interlude or character-animation staging. No director-intent claim is established.

Borrow palette **roles**, not a full-screen neon grade for faces: dominant accent, dark support/outline and a light mark. Veto contrasts a mostly black field against cyan/cream; Game Changers uses several flat saturated planes. Their actual hex values were not calibrated here. Preserve the venue's skin and equipment colors in live footage; restrict a graphic palette to a brief accent when that suits the brief.

Separate three rhythms: camera edits, drawing/shape changes within a shot, and musical attacks. A drawing can hold while an independent camera or plate continues smoothly. For live footage, apply cel timing to the graphic path/precomp, not automatically to the entire camera plate. Avoid using face/body warps to imitate a reference character's hand-drawn exaggeration.

## Music and lyric limits

Nearest full-mix spectral candidates were retained separately from the visual notes. Veto's38.208333 change sits17.003ms after a low-band candidate at38.191330. Game Changers'72.400 graphic change is1.330ms before a snare/onset candidate at72.401330, but the72.766667 shot entry is94.663ms before its nearest broad onset candidate. Other selected entries differ by much more. FFT/HPSS timing, thresholds and effects in the mix remain uncertain. These numbers do not prove listening-approved sync, beat intention or that all cuts should follow bass. No nearby low-band candidate does not prove absent bass.

The cached ASR has no segment overlapping Veto38–41; this cannot establish an instrumental section. The Game Changers window overlaps a long repetitive draft segment, unsuitable for a precise word-to-image interpretation. No phrase was promoted to verified lyrics. For JUMP, keep lyric/image decisions pending rather than using these drafts to invent a reason for a shot.

## Tested original native construction

The resulting study is a rising curved **filled brush form**, not a traced reference drawing. It uses native Shape paths, a dark underprint, a cyan body, transparent scratch channels and separate cream ink flecks. Use AE for editable contour/mask timing; Illustrator or Photoshop would be appropriate for more authored contour/paint texture if that becomes the design need. Those alternative drawing pipelines were not tested in this pass.

The first version passed technical checks but was visually rejected: fourteen regular large diamond openings and three long ridges made it read as a leaf/blade. Preserve that failure as a design lesson. Adding complexity counts is not a substitute for judging the silhouette.

The accepted **technical study revision** has an asymmetric contour,44thin varied channels and12short flecks. It is still a vector brush approximation; the reference's fine hatch/dot-screen and full character animation were not reproduced. It has not yet been placed on moving live footage or judged with music. Do not present it as final art direction.

| Timing/output | Tested values |
|---|---|
| Main preview | 1080×1920, 30fps, 36frames/1.2s, silent |
| Separate alpha | Complete, body and ink; ProRes4444,120fps,144frames each |
| Graphic poses | Delivery frames4,6,9,11,13; all path and scratch keys use HOLD |
| Support | `[4/30,15/30)` seconds; alpha frames16–59 inclusive |
| Handles |16blank alpha head frames,84blank tail frames |
| Pose durations |2,3,2,2,2 delivery frames; deliberately uneven |

Keep support and all component timing identical. True transparent channels allow the next editor's background to appear through them. A dark painted stroke would not do that. The preview's dark background is a separate layer and is absent from alpha exports.

The120fps render preserves the held drawings; it does not invent extra drawings between them. At normal speed in30fps, one main frame corresponds to four alpha samples. Interpreting120 as30fps makes the asset four times longer, including holds and handles. Design any retime intentionally, then recheck its action anchor and cel lengths.

## QA learned from actual failures

- Four outputs were fully decoded; dimensions, frame rates, counts and absent audio passed. All432alpha frames were streamed, including support/blank handles. Every one of the36preview frames and five-pose/negative-space boards was inspected.
- An exact decoded RGBA hash test rejected every held interval. Investigation found tiny pixel differences, not a moving contour. The diagnostic first hold showed RGB differences of roughly0.4–0.46/255 over active pixels, with at most2/255 alpha variation. Quantization or render dither is a possible explanation; the exact stage was not independently identified. Do not report bit-identical holds. The final check records every active held frame and separately bounds alpha, active RGB change and binary-boundary changes.
- Recombining independently encoded body/ink alpha against encoded complete alpha produced a worst observed error just over2/255 on a soft edge. Three quantized streams make an exact/two-code test unsuitable here; keep measured max/mean errors and a declared three-code bound. This is a local verification method, not a universal codec tolerance.
- Thin diagonal scratches are antialiased. A rounded geometric centre measured alpha65 in one case, so an alpha0 assertion at every centre was false. In the revised asset all44channels produced alpha reduction at reviewed probes;39had a fully transparent core within the local3×3patch. Geometric interior plus nearby opaque paint and checkerboard inspection distinguish real cut-through from a blank/broken render. Preserve the other partial-alpha channels in the record.

Do not broaden numerical tolerances to hide a visible defect. Inspect the failing region and state which property the replacement test actually proves. Here technical success did not prevent the first design from being rejected visually.

## Implementation/review prompt

“Use the inspected reference passage for cadence and color hierarchy. Draw one original gesture around the selected action, with an authored asymmetric contour, a limited accent palette and purposeful negative space. Keep cel path changes separate from camera motion. Save all pose/frame coordinates, key interpolation, alpha support and intended playback speed. Render body and light marks independently plus a clean composite. Inspect the silhouette at phone size, actual cut-through on contrasting backgrounds and every entry/exit frame. Preserve rejected versions and numerical warnings. Keep hearing, lyrics, source-project technique and final-style approval separate from a successful render.”

Local evidence: `boards/ref_2FLY-gn-hGQ/Sequence_38.000_3.000_stride1`, `boards/ref_69sKYwsxUM8/Sequence_72.000_3.000_stride1`, `analysis/drawing_pass7`, rejected `native_study_05` and corrected `native_study_05_rev2`. These are local provenance paths, not portable skill dependencies. For attachment to a real moving object, use the separate [moving accent study](moving-accent-study.md); this new asset alone does not establish registration or physical occlusion.
