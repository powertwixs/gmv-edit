# Moving accent, foreground subtraction and honest tracking QA

Verified local native AE study, 21 October 2026. A lime ring and short blue motion trail follow an actual arcade ball in privately supplied camera footage. This proves a small moving attachment and short manual occlusion, not automatic semantic tracking, long roto, a finished GMV design or perceptual music sync. No reference-film pixels were inserted.

## Choose a feature that can actually be followed

The first tan-ball point proposal was rejected: fingers and blur made its centre ambiguous. The magenta ball was more separable. It is held in the girl's other hand; do not infer a second person from a second ball. Source frames94–115 were extracted with PTS and inspected. A color-assisted connected-component detector proposed 18 centres; all candidates were checked in images. Frame111 was rejected because the partly cropped object produced a collapsed radius. Seventeen points94–110 remained, with the graphic ending before frame110 is displayed.

The local detector used HSV hue139–170, saturation85+, value55+, a y350–800 search band at1080×1920, area600–25000px and a continuity gate. These are source-specific search parameters, not a portable magenta-ball preset. Connected-component centroids can follow shadows, a blurred tail or similarly colored equipment. Record source PTS, coordinate space, identity and uncertainty, then inspect the path; do not equate a numeric centroid with a physical centre.

Frames99/100 received an estimated ±20px uncertainty for blur/merged tails; other reviewed points used approximately ±8px. These are working estimates, not calibrated confidence intervals. When the silhouette leaves frame or the detector changes identity, stop the accent or correct from visual evidence rather than extrapolating a confident trajectory.

## Time and coordinates

| Domain | Tested mapping |
|---|---|
| Original | 1728×3072, 60000/1001 fps; first selected plate frame90 at1.5015s |
| Inspection | 1080×1920, exactly62.5% of source dimensions |
| Main | 1080×1920, 30fps, 36frames/1.2s; constant0.5005× playback |
| Attachment | Delivery frame `f` maps to original frame `90+f`; position keys4–20 |
| Graphics | Separate120fps comps and ProRes4444 alpha, 144frames/1.2s |
| Graphic support | `[4/30,20/30)` seconds: alpha frames16–79;16 blank head and64 blank tail frames |

Camera audio is disabled. Source scale62.5%, centred anchor/position[540,960], no camera movement, frame blending or Optical Flow. Native source-time and position properties were audited after construction. Do not reuse the simple coordinate mapping after a crop, parent, transform, stabilization or retime change; transform both the tracking coordinates and foreground matte consistently.

At source59.94 to delivery30fps,0.5005× can use one captured source frame per delivery frame. The120fps graphic interpolates between measured positions; it does not add captured ball detail. Keep the alpha's real-time duration when inserting into30fps. Interpreting120fps as30fps deliberately makes it four times slower and requires a corresponding new plate/anchor mapping. Check the rendered sample sequence after retiming.

## Editable native construction

Use separate comps for clean plate, unoccluded accent, foreground-subtracted accent and main preview. Preserve both control and masked outputs so a disappearing graphic can be localized to the matte instead of misdiagnosed as failed tracking.

The ring is an Ellipse Path with animated position/size, linear temporal interpolation and zero spatial tangents to avoid overshoot. Its radius is the measured component radius plus14px, using a6px stroke. The blue7px trail is an original open four-point Shape Path made from the current position and preceding three delivery-frame positions. Here it was sampled every1/120s; that is a tested construction, not a requirement for every trail. Expose color, stroke width, radius padding, history duration and opacity for design work. Opacity fades near the end; explicit layer in/out prevents interpolation from leaking outside the reviewed support.

The simple ring is a registration diagnostic and basic accent. Before using the method in a final film, design an original stroke silhouette, draw-on/decay and hierarchy for the chosen action. A bright circle around every object would be repetitive and would not reproduce the reference's richer hand-drawn language.

## Short foreground occlusion

On an AV layer containing the accent precomp, a seven-vertex SUBTRACT Mask Path follows the supporting hand/sleeve for delivery frames4–7. Four manual shape keys,2px feather. This is a short animated approximation, not Roto Brush or a long tracked matte. View the visible hand boundary against the clean plate, not only alpha on black.

An initial implementation animated Mask Opacity from100 to0 to remove the subtractor. On the tested AE build this made the entire accent disappear after frame7. Keep this observed failure scoped to that native graph; do not assume all subtract masks in all versions behave identically. The successful revision keeps opacity100, sets the polygon outside the canvas at frame8 and uses an outgoing HOLD at frame7. This avoids sweeping the mask across the image between those keys. A separate overlay segment is another option that would need its own render check.

Validation compared masked and unmasked alpha:646/632/595 pixels above20alpha removed on frames4/5/6; selected foreground samples changed255→0. After frame8 the two alphas were essentially equal. Actual comparison boards were also inspected. A removed-pixel count alone does not prove the hole matches the real hand.

## Three independent questions for QA

1. **Was the intended source frame rendered?** Compare clean native frames with expected and adjacent original source frames. This study used normalized Sobel-gradient correlation in the same ROI, reducing sensitivity to color conversion. Eleven selected delivery frames matched the expected source frame, correlations0.971–0.979 and at least0.861 margin over neighbours. This covers selected frames, not every rendered frame, and is not a universal threshold for low-motion footage.
2. **Was the graphic rendered at its authored position?** Independently decode the control alpha and fit the visible green ring. Nine sampled positions were within0.732px of their native keys. This establishes drawing placement, not the truth of the original ball-centre annotations.
3. **Does the attachment/occlusion look right?** Inspect original point candidates, clean/control/masked comparisons, every delivery frame and alpha on a checkerboard. All36delivery frames were viewed in this1.2s study; source point candidates and difficult overlap frames were reviewed separately. This is visual frame inspection, not continuous AV listening.

A false error exposed the importance of these separate checks. The same HSV detector on an export initially merged the red arcade arch with the ball, shifting a centroid40–55px. Matching the source ROI fixed those instances, but frame13 still had a60.409px diagnostic discrepancy from connected-component merging. The original/native spatial detail and actual ball/ring images matched. The detector warning was preserved; no speculative Time Remap correction was applied. A native frame-rate property rounded to59.940002 is not by itself evidence of a wrong source frame. Do not enlarge tolerances merely to obtain a green QA result.

Fully decode every deliverable; verify dimensions, rates, frame counts, audio absence/presence and all alpha support frames. Both alpha files here were streamed over all144frames: no unexpected early/late opacity. Preserve numeric evidence and explicitly label visual review. Research source fingerprints use size plus first/last1MiB, not a full-file cryptographic identity guarantee.

## Tested native scripting pitfalls

Tested on AE26.5x89. Recheck when porting:

- Adding a property to indexed Shape Contents can invalidate earlier child handles. Add the path and stroke, then reacquire the path/size through its known index or matchName. Keep index assumptions local to the group just constructed.
- The Shape Position property's `keyValue()` returned three elements even for this2D layer. Match the spatial-tangent array length to the returned value; a two-element array failed. Set temporal interpolation explicitly.
- Native position values had about0.000043px floating error. A0.001px serialization audit tolerance was appropriate; a1e-5px assertion falsely rejected correct keys. This numerical tolerance is separate from visual tracking uncertainty measured in whole pixels.
- The isolated ExtendScript runtime did not provide `JSON`; use a tested ES3 serializer or bundled parser. Read only the workflow's own trusted generated plan, not arbitrary evaluated external text.

Run a new `AfterFX.com -m -noui -r` process with a task-specific token, require an empty clean fileless project, and refuse an existing output AEP. Preserve failed attempts and choose a new revision folder. A new process flag alone does not replace the guard. Do not attach a research generator to the user's open Premiere/AE work.

## Next-editor brief

“Inspect the chosen moving feature through preparation, release and exit. Save original path/fingerprint, PTS, coordinate transform, reviewed point uncertainty and separate cut/action/graphic times. Make a clean plate, unoccluded control and short foreground matte as editable AE layers. Keep camera FPS, generated-graphic FPS and delivery FPS distinct. Verify actual source-frame selection, authored stroke placement, alpha lifespan and physical overlap separately. Preserve detector warnings and rejected samples. Deliver native source and separate alpha assets; do not label this a finished GMV or hearing-approved sync.”

Local evidence: `native_study_04` contains rejected proposals and the failed first mask render; `native_study_04_rev2` contains the corrected AEP, five outputs, `QA.json`, `Source_Frame_Matches.json`, comparison and consecutive-frame boards. Scripts live in the lab's `scripts` folder. Those local paths are evidence for this study, not dependencies of a portable skill. Music-backed action sync is a separate [tested workflow](action-anchor-workflow.md).
