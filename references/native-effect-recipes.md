# Native effect design and tool selection

These are implementation recipes, not claims that an AE study was rendered and approved. Recheck installed versions and available controls. Keep editable comps/layers and handles. Use the supplied template project when its actual design is the reference; inspect and relink its media/control comps before changing it.

## Choose the application by the work

| Work | Preferred starting tool | Reason / limit |
|---|---|---|
| Music mapping, story cuts, action timing, native clip color | Premiere Pro | Preserve source in/out, tracks and practical re-editability |
| Tracked drawn strokes, silhouette matte, graphic impact, template intro | After Effects | Shape paths, parenting/tracking, roto and layered timing; actual template work belongs here |
| Original static textures, subject cleanup, drawn assets | Photoshop / Illustrator | Raster paint or editable vector paths; maintain layers/SVG |
| Real depth, a modeled object and camera interaction | Blender if available and necessary | Do not rebuild a simple 2D accent in 3D just for tool prestige |
| Invented standalone illustration/texture | Image generation when useful | Suitable for bitmap concepts; no promise of stable frame-to-frame subject identity |
| Technical evidence, audio candidates, QA | FFmpeg + Python | Reproducible measurement and extraction; numerical metrics do not replace taste/listening |

Check the installed editing applications and versions. Installation is not proof a specific effect/plugin/render works. Do not disturb an unsaved live project to run a study.

## A. Pose-preserving graphic punch

Reference relationship: PARANOIA 22.416667–22.583333. Make an original variation, not a traced reference character.

1. Choose a readable pose/contact frame in the user's shot. Prepare its alpha using roto or a manual matte; inspect hands, hair, gaps and blurred edges on contrasting backgrounds.
2. Keep subject position and silhouette consistent with the live plate. Put background, fill silhouette, outline and original hatch/stroke marks in separate comps/layers.
3. On the selected accent, replace the live color with a controlled graphic palette for roughly 0.12–0.20 s as a starting study, then return to the action. Use source-derived pose and a short handmade smear if needed.
4. Animate silhouette/outline independently: tiny registered displacement, brief edge expansion, stroke draw-on. Do not animate an entire poster floating away from the shot.
5. Check the resolved live frame at normal size. If the face reads as warped or the matte chatters, fix the source/roto before adding texture.

## B. Tracked drawn gesture

Draw an original curved arrow, starburst or movement trail as an AE Shape Path. Animate Trim Paths for a 2–4 delivery-frame draw-on and a 2–5 frame disappearance; these are starting values, not universal timing. Track/parent to the relevant hand, ball or landing area. Animate a small path variation on selected frames if a handmade boil is appropriate; avoid random flicker on every property. Put stroke below the subject or mask its overlap when the physical occlusion requires it. Check entry/exit tangents and keep faces unobstructed.

A short real-footage ring/trail with animated foreground subtraction now has a [native render and QA study](moving-accent-study.md). It tests attachment, alpha timing and a manual hand holdout; it does not validate every gesture/Trim Paths design described above.

For a filled, deliberately held drawing rather than a continuously revealed line, see the tested [brush language study](brush-language-study.md). Separate body, cut-through channels and light flecks; check the silhouette as well as masks. The native asset has not yet been registered to moving footage.

## C. Directional smear into a clean shot

Reference relationship: PARANOIA 57.875–58.125. Mark three events separately: graphic departure, streak/occlusion, resolved new view. Carry exit direction into entry. Use original stroke paths and a controlled directional blur for the brief bridge. Start the first readable incoming frame on the intended music attack. Derive overscan from actual movement/crop; never hide black edges with arbitrary soft borders. Remove the effect after it serves the transition.

## D. Impact from an actual origin

Reference relationship: weapon light -> reaction in Warriors and Wasteland samples. For live venue footage, anchor a small burst/ring to ball/pad/foot contact. Build 3–6 irregular Shape Paths with fast extension and slower short decay; matte behind the subject where appropriate. Keep a clean plate underneath. The contact, burst onset, camera cut and reaction may use different frames. Do not add reference weapons/fire or false venue events.

## E. Brief time/graphic echo

Reference relationship: Enemy 174.542–174.708 sampled colored silhouettes. Derive a clean subject matte; offset one or two duplicate silhouettes by a purposeful short time/position interval and color them as accents. Keep the primary subject dominant and return to a single readable body. Verify foot/hand continuity; overlapping children are a difficult matte and may warrant choosing a better shot.

## F. Intro/logo and separated assets

When the user supplies an AEP, inspect its master, media replacement, background, logo and render comps; preserve animation structure that gives the reference its look. Replace media in source comps rather than imitating the finished frame with a basic scale. If separate assets are requested, render background, subject, crown/strokes and accent groups independently, each with its own animation and consistent duration/origin/handles. Alpha MOV or PNG sequences need explicit straight/premultiplied interpretation checks. Deliver the AEP and layer manifest with the renders.

## FPS and speed

Do not conflate capture FPS, AE sampling FPS, Premiere sequence FPS and export FPS. An AE 120 fps procedural stroke can offer finer retiming samples. A 30 fps live-action plate stays limited by its captured frames. 59.94 and 60 are different rates. Decide the delivery rate, source conform, retime curve and handles together; document interpolation. Inspect frame sampling/blending/Optical Flow on difficult edges rather than promising smooth slow motion from a high export FPS alone.

## Color

Normalize exposure/white balance/transfer first, match neighboring shots second, apply a restrained shared look third. Protect skin and the venue's actual colors. Use a reference palette for a brief graphic accent without making all live faces neon. Check HDR phone material in an actual SDR export. Comparison View/Color Match is a starting point, followed by shot-specific correction; automatic matching is not final approval.

## Official implementation references

- [AE shape and mask path animation](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animate-shape-paths-and-masks/animating-shape-paths-masks.html)
- [AE Roto Brush and Refine Matte](https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/roto-brush-refine-matte.html)
- [Premiere time interpolation](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/apply-time-interpolation-methods-to-adjust-clip-speed.html)
- [Premiere Color Match and curves](https://www.adobe.com/learn/premiere-pro/web/color-match-and-curves?learnIn=1)

These document features; the specific recipes above still require a native render and visual review on the user's footage.
