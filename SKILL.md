---
name: gmv-edit
description: Analyze GMV, Arcane, Jinx and game music video references and edit raw footage to music. Use for reference breakdowns, bass/action synchronization, lyric-aware shot choices, pacing, original drawn accents and native Adobe effects while preserving editable sources. Do not use for unrelated slide shows or avatar videos.
metadata:
  version: "0.1.0-beta"
---

# GMV Edit — Beta 0.1

Build a music-led sequence from inspected raw footage. Transfer the reference's timing, action continuity, and transition behavior to the user's subject. Reference movies provide editing evidence; they are not footage to insert unless the user requests it.

## Confirm the creative scope

An independent mixed-game GMV uses the game/animation sources selected for that brief. A venue promo uses the allowed camera footage. Do not turn a new independent project into a re-score of an existing client edit. Confirm source category, aspect, music excerpt and editable application from the actual request.

Separate inherited animation/VFX in supplied films from newly authored cuts, masks and graphics. A static pose matte is not long tracked roto or original character animation. Use supplied media only within the user's authorized scope.

## Default duration: complete music, no cuts

- If the user gives no duration limit or music range, build the edit across the **entire supplied music track, from beginning to end**. Keep the musical intro, breaks and outro. There is no automatic 35/45/60-second cap; another project's Reel brief does not apply. A request to test the skill also does not authorize a shorter song excerpt.
- In a full-track job, keep the music continuous, in its original order and at its original speed. Do not trim the head/tail, skip sections, loop, rearrange, insert dropouts, time-stretch or add an early fade to fit a shorter montage. Retime and cut the visuals to the music.
- A user-requested shorter duration, source excerpt, preview or specific editable timeline interval overrides the default for that task. Preserve all protected regions and the user's existing audio. Reference-analysis windows and short effect studies are technical scopes, not delivery-length limits; a partial test must be labeled with its range and must not substitute for the full requested edit.
- Probe the actual audio extent and plan visual coverage for the whole track before editing. Round video length up to the delivery-frame boundary so the last audio sample is covered. Correct codec/native-app delay using appropriate padding and PTS-aware alignment; do not discard real opening or ending music samples to hide an offset. Verify complete decoded audio coverage in the final export.
- If the full edit remains unfinished, keep a checkpoint and label any partial output incomplete. Time, render or token limits do not authorize silently shortening the song or presenting a shorter preview as the completed deliverable.

## Choose the workflow

- For learning or a reference breakdown, read [research protocol](references/research-protocol.md) and [measured examples](references/measured-examples-2026-10-20.md). Establish evidence before writing a treatment. Research is not permission to change the live edit.
- For the expanded 25-reference library, additional every-frame drawings, provisional lyric readings and verified native tool behavior, read [second study pass](references/study-update-2026-10-20.md).
- For footage editing, follow the sequence audit, source selection, rhythm and verification steps below. The current brief decides whether graphics are allowed.
- For requested drawing/compositing, use [native effect recipes and tool selection](references/native-effect-recipes.md). Effects are not mandatory on every cut. The raw-footage-only restriction below applies only when that is the brief.
- For a tested live-footage manual mask, short pose hold, clean return and native alpha export workflow, read [real-footage pose study](references/real-footage-pose-study.md). It includes a rejected source and a corrected matte failure; do not mistake a single-pose study for tracked roto.
- For separate cut/action anchors, supported slow preparation, native audio-offset correction and a tested music-backed study, read [action anchor and audio sync workflow](references/action-anchor-workflow.md). [check_action_anchors.py](scripts/check_action_anchors.py) audits plan arithmetic and capture-rate limits; it does not certify perceived rhythm.
- For a 20-second consecutive-frame narrative study, changing shot cadence, repeated flashes within one shot and motivated occlusion, read [narrative continuity study](references/narrative-continuity-study.md). It separates observed edit behavior from possible intent and gives an action-sequence adaptation template.
- For a tested moving-object stroke, short animated foreground subtraction and 120-to-30 fps alpha workflow, read [moving accent and occlusion study](references/moving-accent-study.md). It includes detector failure, independent source-frame checks and native Shape-property pitfalls; the simple test graphic is not a finished visual style.
- For observed held-drawing cadence, palette roles and an original filled brush with transparent channels, read [brush language study](references/brush-language-study.md). It includes a visually rejected first design and separate body/ink alpha verification; reference authoring software and lyric sync remain unverified.
- For readable preparation shots, localized highlights and manually annotated attention/color checks, read [color and attention study](references/color-attention-study.md). Its tested region helper reports image proxies and editorial points; it does not grade footage or infer viewer gaze.
- For continuation, read the project's checkpoint and coverage ledger before repeating any analysis. Keep incomplete listening, ASR verification and untested recipes visibly pending.

Reusable tools: [reference_window.py](scripts/reference_window.py) extracts consecutive frames with source PTS; [music_candidates.py](scripts/music_candidates.py) produces provisional low/high percussive attacks and tempo candidates. Both require a separate empty output folder, preserve originals, and record that inspection/listening is still required. See [research protocol](references/research-protocol.md) for commands and interpretation.

## Establish the actual edit

- Inspect the live project before assuming the last export is current. Snapshot sequence frame rate/timebase, clip source in/out, speed, effects, track mutes, music edits, gains/keyframes, and the requested editable interval. A new song can be on a different audio track while the old one remains muted.
- Save a new native project copy with the user's latest unsaved changes. Leave protected opening/tail regions and music intact unless asked to change them. Preserve frame-exact boundaries, including source offsets when splitting a boundary clip.
- Read timecodes using the sequence rate and drop-frame setting. Never treat `09;04` as 9.04 seconds. At 29.97 fps in minute zero, `00;00;09;04` is frame 274 and `00;00;55;25` is frame 1675.
- Respect the current brief's exclusions and person/group limits. Do not make one project's date restrictions universal.
- Reconcile live user deletions against the last plan before rebuilding. Keep an exclusion log with original file and source range; do not restore a deleted selection by rerunning an older generator. Check for further live edits immediately before applying a timeline rebuild and stop to reconcile if the snapshot changed.

## Learn the supplied references

Inspect at least one build and one active musical passage. Extract both a broad contact sheet and a dense 0.1-0.25 s sequence around transitions. Record exact source timestamps and what is visible. Scene-change detectors identify candidates; camera movement and flashes can produce false detections.

Distinguish three things: shot duration, subject movement inside a shot, and an added transition. A long moving performance shot is not evidence for cutting every beat. A hard impact cut does not require a permanent distortion effect.

Analyze a sustained 15–25 second passage as well as isolated accents. Mark anticipation, action, payoff and reaction, and record partial shots at the passage boundaries. Check whether flashes occur inside a continuing shot. Full-mix low-frequency peaks may include sound effects; a nearest-peak match alone cannot establish musical intent. Preserve ambiguous camera traversal/hidden-cut events as uncertain.

For the user's established reference library and observed examples, read [reference notes](references/reference-notes.md). Reinspect local files if they change or the new brief emphasizes another passage. Never claim full audiovisual viewing from contact sheets.

For a developed reference study, inspect an overview across the entire duration, then contrasting build/action/recovery passages, then every source frame around selected accents. Record actual source PTS. A two-frame sampling interval cannot prove a one-frame effect's duration. Separate `cut`, `in-shot impact`, `drawn overlay`, `camera move`, `lighting change` and `uncertain` events. See the measured PARANOIA examples: a four-frame graphic insert can happen inside one continuing performance shot, while a rapid camera exit can span several distinct musical attacks.

For lyric-to-image work, first verify the audible phrase and its time range. Describe its function (challenge, preparation, release, reaction, identity, contrast) and select an action that serves it. Do not force literal illustration of every word. Attribute a creator's intention only when documented; otherwise label it a possible reading with alternatives. Singing ASR is a search aid, not a verified lyric transcript.

## Find useful action

- Probe originals for duration, orientation, frame rate, and colour transfer, then inspect several moments. File names and shooting dates do not prove the activity or venue.
- Make a selected-source log with source in/out, activity, visible people, framing, useful action/landing, and any exclusion flags. Choose an action whose preparation and payoff fit the musical window.
- Rotate wide activity, medium action, detail, and reaction. Match a ball strike, jump, landing, reach, turn, or camera direction into the next shot. Avoid repeatedly returning to the same person or nearly identical angle.
- When action sync is disputed, inspect the action densely at 0.05-0.15 s intervals. A shot midpoint or an activity label cannot establish the exact contact/landing frame. Check preparation, contact/apex and recovery; never label a walk through a foam pit as a jump without seeing it. Cut-onset accuracy and action-onset accuracy are separate checks.
- Prefer an occupied game to an empty equipment pan. A drone shot must stay visibly inside the allowed venue; a panorama that crosses an adjacent corridor is not automatically acceptable.

## Build rhythm around the actual song

Analyze the audible music region after its source in-point and edits. Estimate tempo, then inspect onsets and musical phrases. Snap deliberate cuts to actual attacks within roughly one delivery frame rather than imposing a fixed numerical cadence.

If the user asks for bass synchronization, isolate roughly 30-200 Hz and inspect rising edges with a short envelope. Broadband spectral flux can follow vocals or snares instead. Analyze the actual current export when available, or verify source-to-export audio delay. AAC encoding and analysis windows can shift apparent attacks. Treat the beat grid as a guide, then choose actual attacks; do not invent bass hits in a break where the low-end has dropped away. Use vocal or phrase changes and longer action holds there.

Keep the intended decoded-audio excerpt and native application in-point distinct when a measured import offset exists. Cross-correlate the rendered waveform against that intended excerpt, correct only the measured offset, re-export and remeasure. A local study needed 21.333 ms correction; this is evidence for measuring, not a fixed compensation to apply to other projects. Frame arithmetic within one frame does not remove onset-detection or action-classification uncertainty.

Use a phrase-shaped rhythm: readable action, a short burst, a payoff, then breathing room. Typical starting points are 1-3 beats for an action shot and occasional half-beat details. They are not quotas. Let important actions complete; avoid a monotonous series of equal-length cuts.

Select the source action and playback speed before setting the visual hit. Use slow motion mainly when source FPS supports it (59.94 source -> 29.97 delivery can support 50% speed). Speeding a long shot or slowing a repeated frame does not create a new action.

Keep source, composition and delivery rates separate. For regular captured motion without interpolation, minimum real-time speed is approximately delivery FPS / source FPS. A 120 fps AE render of 30 fps footage adds timing samples for generated animation; it does not invent captured subject detail. If graphics are retimed, retain the AE source, render handles and log the intended playback speed and alpha interpretation. Verify Optical Flow on hands, hair, fences and fast motion before relying on it.

## Keep transitions brief and footage readable

When the brief asks for raw-footage GMV editing:

- Keep each visible middle-section clip linked to its original camera file. Use native scale/position, speed, colour, and blur controls. Do not replace the sequence with baked full-frame AE composites, stock graphic cards, or footage from the reference videos.
- Make most cuts direct. Reserve 2-6 frame zoom/whip/blur accents for selected hits and phrase changes. The stable part of the shot must return to clean, recognisable footage.
- For a sharp bass hit, put anticipation/blur in the outgoing 2-4 frames and make the incoming shot sharp on its first frame. A transition that only becomes sharp three frames after the bass feels late even when its edit point is on the beat. A short scale settle may follow the hit; avoid continuous pumping on every detected low-frequency fluctuation.
- Match exit and entry direction, centre of attention, and scale. Use overscan when moving an image so edges do not expose black. Blur covers a transition, not poor framing.
- Preserve faces and bodies: no liquify/fisheye bending, unmotivated shaking, rolling warp, or permanent chromatic splitting. Add no text/logos or background designs unless requested.
- Compare brightness and skin tone across adjacent shots. Avoid using contrast or saturation as a substitute for timing. If HDR phone footage is used, verify native tone mapping in an exported frame rather than trusting a washed-out thumbnail.

For native Premiere implementation pitfalls, load [Adobe notes](references/adobe-notes.md). Use AE only when the requested effect actually needs it; the user's choice of editable application takes priority over a code-rendering default.

## Verify the deliverable

1. Audit the timeline against the plan: exact editable interval, original media paths, no gaps, no forbidden event/venue shots, limited repeated people, and unchanged protected regions/audio.
2. Export a draft and inspect every cut's settled frame plus dense frames at special transitions. Fix empty scenes, cut-off subjects, black edges, unintended blur holds, and missing layers.
   When reducing crop/scale, recheck transformed source coverage and the whole shot's recovery. Two renders can match while sharing the same exposed edge. Dark subject backgrounds can conceal a black strip in thumbnails.
3. Export the corrected sequence/selection. Decode the entire MP4; verify dimensions, exact frame count/FPS, audio channels, loudness and true peak. Measure the final audio, not only its source. For a full-track job, verify the original beginning, ending and every intervening music section remain continuous and the video covers the complete audio extent. Preserve user music/gain unless a correction is needed and authorized.
4. Deliver the native project, a usable review MP4, and any necessary editable effect source. Clearly mark a middle-only preview and its original timeline range. Keep the part the user will finish untouched.

Report only what was verified. A valid XML/media-link check alone does not prove a native render; an inspected contact sheet does not prove uninterrupted playback.
