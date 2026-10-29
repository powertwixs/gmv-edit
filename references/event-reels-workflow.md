# Event Reels: speech, continuous music and moving subjects

Use with the parent skill and Reels submodule when the brief combines event footage, original speech and music. These notes come from local Premiere revisions completed in October 2026. They describe tested decisions and failure corrections; they do not establish one mandatory scene order, a default short duration or a promise of virality.

## Establish the current version and opening

- Inventory the actual sources: duration, orientation, source/nominal FPS, audio channels and HDR transfer. Inspect a broad overview, then denser candidate windows. Listen to speech and music with available playback tools. ASR is provisional, especially for names and singing; contact sheets alone are not audiovisual review.
- Read the latest feedback and compare it with the current exported opening. A screenshot may identify a moment inside a clip, not the beginning of its file. Match it visually, inspect the preceding action and keep the requested moment when changing the lead-in.
- Separate requests for a new edit, an opening replacement and a music-only revision. A narrower revision should preserve approved audio and unaffected timeline regions. Compare decoded audio when it must remain unchanged; file hashes may differ after encoding.
- Save a separate revision. Record the final source intervals, exclusions, musical mapping, crop endpoints and protected sections in the authoritative plan. Update that plan after manual polishing. Do not rerun an initial generator whose framing/selection is obsolete.

## Build a story before filling the duration

Choose an opening that is readable immediately and fits the current brief. An occupied group, stage entrance, gesture or completed action can establish energy; no specific child, flag, drummer or crowd is a universal opener. Alternate purposeful wide/group, medium, detail and reaction views without repeating the same crop as though it were another camera.

If speech carries the opening, preserve a complete thought. A J-cut can begin the sentence over relevant room/group footage, then reveal the speaker at the matching original source time. An L-cut can carry its end over a cutaway. Compute picture/voice source mapping explicitly so the visible mouth remains synchronized. Avoid cutting syllables or accelerating a sentence merely to satisfy a cap. Reduce redundant pictures or choose a shorter complete thought instead.

For a user-authorized short Reel, choose one coherent music excerpt with a readable beginning and musical ending. Keep its order and speed. Treat the excerpt as one continuous bed unless the user asks for another musical structure. For an unspecified duration, the parent's complete-track rule still applies. A prior 59-second brief is scoped to that project or an explicitly continued series, not every future edit.

## Keep audio intentional

- Use separate music and original-speech/performance stems. Decide which source sound serves each section; random camera audio appearing at every picture cut creates distracting starts and stops.
- Under a sentence, lower the continuous music enough to understand the voice, then return smoothly to the musical level. Use gradual gain changes and short boundary fades appropriate to the material. Do not restart the song on each new shot or abruptly open and close the ambience.
- In the tested short opening, music stayed continuous while one complete sentence played for 3.9 seconds. A roughly 17 dB reduction under that voice and a 0.5-second recovery worked for that recording. These are case values, not a preset for different voices or songs.
- Prefer normal stereo WAV stems for native assembly when that route is verified. Check both rendered channels: a prior interchange route produced one-sided playback despite a nominal stereo container. Mono source speech may be centered intentionally; a stereo music bed should not lose a channel.
- Measure the final encoded mix against its intended master. The verified local export needed a measured AAC/native offset correction; never reuse 21.333 ms as a universal delay. If remuxing corrected audio with native picture, retain the native video stream, recheck duration/PTS and compare decoded picture samples. A remux does not prove the native project itself has correct stems.
- Choose loudness for the brief and voice intelligibility. Around -14 LUFS and true peak below -1 dBTP are useful delivery starting points, not creative approval or a platform guarantee. Preserve an approved music gain when the revision does not authorize changing it.

## Crop the subject through the whole action

First select the useful source time and subject. For a dance pair, inspect both people during preparation, turns and recovery; a crop that follows only one dancer can cut off the other. For a choir, a foreground conductor may obscure faces even when the frame is technically filled. Choose another range, a cleaner group crop or a wider composition according to the shot's purpose.

Check first, middle, last and action-extreme frames. Add restrained eased Position keys only when the subject actually travels. Avoid a constant sideways pan that makes a stationary group slide through the screen. If more scale is needed for a group, consider source resolution and readability before increasing it.

In one 3840x2160 to 1080x1920 case, 88.8889% filled the vertical height. Some choir selections required a tighter 125% group crop; dance crops were instead repositioned to keep the pair readable. Neither scale nor pixel center should be copied to other media without checking source size, rotation, anchor and Motion behavior.

## Grade and verify the actual native output

HLG/Dolby Vision camera footage can look wrong in an SDR workflow even when thumbnails appear plausible. Set and read back the intended sequence working color space, native tone mapping and gamut compression, then inspect exported skin, bright clothing and shadow detail. Color metadata tags alone do not transform HDR pixels. Use restrained per-shot correction rather than one aggressive grade across all lighting.

Inspect a draft at all shot entries, representative middle/out frames and critical movements. Correct framing/occlusion before the final export. Technical equality between a render and mux does not detect a crop error shared by both.

Save the delivery project, then independently reload its sequence into a separate QA project or reopen safely. Match active project and sequence explicitly when multiple documents are open. Check source links, exact in/out/start/end, speed, stereo stems, grade and Motion samples against the final plan. Full MP4 decode, black-frame search, dimensions/FPS/frame count, loudness/peak and audio correlation complement visual review; none replaces the others.

## Recorded case and evidence boundary

A local school-event delivery used three original 4K camera files, 16 native video selections and two stereo audio clips. The 54.000-second 1080x1920/30 fps output contained a continuous march excerpt at original speed, choir/stage/dance footage and a complete spoken sentence. Its final QA recorded 1620 frames, -14.17 LUFS, -1.71 dBTP, measured 0 ms audio offset with correlation about 0.999984, no detected black intervals and no decode errors. Six sampled decoded pictures matched the native render after audio remuxing. A saved-sequence import and separate Motion readback found no missing media or plan mismatches.

The initial draft's foreground obstruction and moving-pair crops were revised after visual inspection. This supports the review method; these measurements do not establish continuous audiovisual viewing, audience response, client approval or performance by another agent. This repository update does not rerender that private project. No camera media, soundtrack, private project, client messages or local account paths are distributed here.
