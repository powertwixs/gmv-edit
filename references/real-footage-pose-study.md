# Native real-footage pose study, 2026-10-21

Read when adapting a short illustrated accent to live action or diagnosing matte/retime mistakes. This is a small reproducible technical/creative study, not an approved final GMV look.

## Source selection changed the result

Two privately supplied camera clips were inspected densely. Anonymous clip G105 has a boxing gesture around 2.30–2.49 s. Its rapidly moving arm is heavily blurred and a foreground person overlaps the subject. It was rejected for this first manual matte experiment. Adding more stroke/glow would not repair that selection problem.

Anonymous clip G124 has a clearly separated airborne/tucked pose near 4.45445 s (source frame about 267 at 60000/1001 fps). Hands, head and knees are readable against the trampoline. This is an apex/tuck accent, not a landing or ground-contact event. Use the correct action label when aligning it to music.


## What was built

- Native AE project linked to the original video. No user Premiere sequence or existing AEP was rebuilt.
- Main sequence 1080x1920, 30 fps, 2.2 s. Graphic insert at 0.600–0.766667 s: five delivery frames.
- Subject is a manually drawn native Mask Path on the real frozen frame; outline and original gesture trails are editable Shape Paths. Background, subject alpha and drawings have separate 120 fps comps/exports. This is a single-pose matte, not tracked Roto Brush or newly captured 120 fps motion.
- The source plate is reframed with known dimensions/scale/position so that it covers the whole frame. The subject's silhouette stays registered across clean footage, graphic insert and return.
- The source time map holds the pose during the insert and resumes from that same source frame after it. The five-frame editorial hold consumes time; it must be budgeted into a musical phrase rather than secretly shifting a protected edit or soundtrack.
- The study has source camera audio disabled; it is for visual evaluation. Do not interpret it as a musically verified JUMP edit.

## The first matte failed visibly

The initial contour bridged the head and bent forearm, retaining a triangular piece of trampoline background. The correction followed the concave neck/shoulder/forearm boundary and used small Bezier tangents. Review negative spaces, not only the outermost bounding box. A connected outer contour must trace open concavities; enclosed holes require subtractive masks or a proper matte. Hair and motion-blurred limbs need suitable soft detail or a different source pose.

Check at original output resolution on a contrasting background. A thick outline can hide a small edge error but cannot justify a large background patch. Keep the earlier version for comparison and re-render the correction before declaring it fixed.

## Verified local implementation lessons

- Removing every Time Remap key in AE disabled/hid the property in this build; subsequent setValueAtTime failed. Enable time remapping, replace/add the desired keys while at least one exists, then remove only surplus default keys. Set interpolation deliberately; linear source-time segments preserve constant source playback, while equal-value keys create the hold.
- `High Quality with Alpha` rendered ProRes 4444 directly to MOV; `High Quality` rendered ProRes 422. This avoids an unnecessary uncompressed TIFF sequence. Probe the actual codec, frame rate, frame count and alpha samples instead of relying on the template's name.
- Keep audio disabled on isolated visual/alpha elements when they should not carry camera sound. Otherwise a short frozen subject asset can unexpectedly include ambient audio.
- Export a clean comparison with the same crop/time map. Compare the last pre-insert and first resolved frames plus several later frames. H264 encode differences are expected; compare structure, source pose and modest pixel-error tolerance, not bit equality.

## Two non-flash reference windows

These were inspected at every source frame; audio/lyrics remain unverified.

- PARANOIA 132.333333–133.291667: driver close view through 132.750000; direct cut to a rear-view mirror at 132.791667. The mirror is a detail motivated by the same driving situation. Low-band attack candidate at 132.82133 is about 29.7 ms later; this does not prove perceived sync or author intent. Adapt the main-action-to-related-detail relationship, not the mirror prop itself.
- Enemy 85.083333–86.041667: face observation through 85.500000; a direct cut at 85.541667 opens onto two characters and a moving cloth/action. Warm setting/color continuity and a change of shot size keep the sequence readable. Possible reading: show what the close reaction relates to. Do not claim that reading is documented creator intent or that a particular lyric caused the cut.

The lesson is not to remove effects. Give some beats to action and some cuts to related details/reactions so that the short graphic accents have contrast and meaning.
