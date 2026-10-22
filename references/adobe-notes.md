# Native Adobe notes

These are locally verified implementation hazards; recheck tool support in a new session.

- Premiere `VideoTrack.overwriteClip` can add source audio even when inserting on a video track. Lock/protect all populated original audio tracks; snapshot mutes and clip volume keyframes. Remove only newly introduced audio clips from tracks known to have been empty. Restore lock state. Do not delete or mute the user's music to hide the accidental audio.
- Set imported AV project-item in/out with media type 4 (both) before overwriting. Setting only the video in/out can leave source audio at zero and offset the inserted image.
- Use `Time.ticks` and sequence `timebase` for frame positions. Set speed first, read back the actual speed, and verify the component's keyframe clock on a short render. Do not assume the resulting `inPoint.seconds` is the original captured-source time on retimed clips. See the version-specific verification below before batching retimed effects.
- Public TrackItem has no reliable `setSpeed` in the local bridge. The verified QE call is `qeClip.setSpeed(multiplier, '', false, false, false)`. Match the QE clip by unique clip name rather than assuming item indices match across gaps. Recheck start/end and speed after applying it.
- Add native effects only through verified QE effect names, then inspect the actual public component property list; do not assume a localized UI label/property index.
- Avoid saving over current/previous sources. Native Save As, an actual export, and checked media paths provide different evidence. A native export may omit a Dynamic Link layer although media paths are valid. If the user supplied an approved opening render, place that on an upper track while keeping the native source layers underneath; disclose it.
- Whole-sequence export and in/out export can differ by a frame in the bridge. Probe the actual exported frame count and correct the export range before delivery. Do not infer duration solely from the export API's success string.
- The local native EPR can omit BT.709 H264 VUI; remux `h264_metadata` plus colour flags without a needless second video encode when correcting metadata only.

## Premiere 26.5.2 retimed effects: historical local test

- On these newly inserted raw clips, setting Motion and the locally resolved `Directional Blur` keys at `clip.inPoint.seconds + localSeconds` made some sped-up clips blurred through their entire shot. The resolved blur exposes `Angle` and `Amount`, rather than the older `Direction` / `Blur Length` property names. Always inspect the actual component.
- Corrected key time in this tested context: `(clip.inPoint.seconds + localSeconds) * clip.getSpeed()`. This maps the API's retimed in-point back to original source time. Native exports then showed clean settled frames, blur only in the last three outgoing frames, and sharp incoming frames. This is observed local behavior, not a universal promise about every effect, speed ramp or Adobe version. Verify a first, settled, penultimate and incoming frame before applying it to many clips.
- One requested 1.6x segment, only 14 delivery frames long, read back as `1.42307692307692`. Dividing the original source in-point by the requested 1.6 would have broken action continuity. Use the measured speed to set the API in/out and assert the resulting physical source interval. Record requested and measured speeds separately.
- A same-source slow/fast join needs continuous physical source time and matching image scale at the join. A keyed push on the slow section and a reset scale on the fast section creates a framing jump even when the source is continuous.

## Isolated AE study, verified on 26.5x89

- CLI `AfterFX.com -m -noui -r <jsx>` was tested with a task-specific inherited environment token and an empty/pristine-project guard. Probe the token, project file, item count and dirty state before any mutation. A plain `-r` may target an existing instance; it is not proof of isolation. Do not use a new-instance assumption to close/save over someone's work.
- Self-contained CLI ExtendScript did not provide `JSON`; bridge-injected conveniences are not portable. Use a local serializer/polyfill in standalone JSX. ES3 syntax is required.
- Shape Group transform scale match name is `ADBE Vector Scale`; `ADBE Vector Group Scale` returned null locally. Inspect actual properties instead of guessing names.
- Enumerate output module templates. PNG Sequence was absent; TIFF Sequence with Alpha existed and rendered four channels. `setSettings({'Channels':'RGB + Alpha'})` failed because the property was read-only. Applying the available alpha template worked.
- That TIFF render used ExtraSamples=0 despite four sample bytes. Pillow's RGB mode alone falsely suggests no alpha. FFmpeg reported RGBA; direct byte/alpha checks were needed. Document interpretation and check a composite over both light/dark or checkerboard backgrounds.
- Image sequence imports need an explicit rate. A 120 fps comp's TIFF/PNG files carry no reliable movie timebase; FFmpeg's default image-sequence rate can silently create a slow/duplicated derivative. Probe frame count/rate of the derivative and inspect actual alpha samples.
- In the real-footage study, removing every Time Remap key caused the property to become hidden and later `setValueAtTime` failed. Add/replace intended keys while a key remains; remove surplus default endpoint keys afterward. Equal source-time keys create a hold; use deliberate source-time interpolation for normal playback on either side.
- Direct `High Quality with Alpha` MOV rendered ProRes 4444 with alpha locally. `High Quality` produced ProRes 422. Recheck these templates on another installation. Disable source-layer camera audio for separate visual/alpha assets when no audio is intended.
