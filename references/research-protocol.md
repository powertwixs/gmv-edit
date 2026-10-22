# Evidence-driven GMV research

Version: 2026-10-20, ongoing study. A stronger instruction file does not train new model weights. It persists reusable observations, methods, tools and acceptance criteria.

## Preserve and inventory

1. Read the current brief, allowed source roots, exclusions, protected ranges and requested native application. Snapshot the live project only if production work is requested. Research should not disrupt another editor's project.
2. Inventory duration, video/audio start PTS, nominal/average FPS, dimensions, orientation, transfer characteristics and stable file size. Wait for downloads/conversions. An MP4 with a valid moov atom can still be growing.
3. Identify references by stable ID and content fingerprint, not only title/path. Recheck size and mtime after analysis. Bind audio, scene metrics, frames and transcripts to that fingerprint. Never reuse analysis from a file replaced under the same name.
4. Keep originals read-only. Derived analysis may be regenerated; retain provenance and completed-work checkpoints.

## Coverage levels

Track each level separately per file. Do not collapse them into one `reviewed` flag.

| Level | Evidence | What it permits |
|---|---|---|
| Inventory | ffprobe + fingerprint | Technical source description |
| Overview | Actual inspection of spread-out frames | Palette, subject and broad composition observations |
| Dense sample | Timed local frame sequence | Local action and candidate transition description |
| Every-frame window | Consecutive source PTS + viewed frames | Frame-local order and effect duration |
| AV passage | Watched/listened at normal speed, then stepped | Perceptual music/image relationship in that passage |
| Lyric verification | Audible words/time checked | Specific lyric/action reading |
| Full AV | Uninterrupted review recorded | Whole-film flow critique |

An automated pass through every decoded frame is not human review of every frame. An overview across the duration is not full AV review. Scene detectors misclassify impact flashes, strobing and camera motion as cuts. Record uncertainty and revisit.

Classify the reference itself before borrowing its cadence: music/performance video, fan GMV, dialogue/action cinematic, hype film, or static artwork with music. Dialogue-led reaction cuts and musical attack cuts serve different timing. The title card inside a film does not establish the film's name. Read the actual file metadata/inventory.

## Portable commands

Run through an available Python with the listed libraries; these scripts do not install packages:

```powershell
python "<skill-folder>\scripts\reference_window.py" "<reference.mp4>" --start 22.3 --frames 24 --output "<new-output-folder>"
python "<skill-folder>\scripts\music_candidates.py" "<music.mp4>" --start 32 --duration 8 --output "<another-new-output-folder>"
```

Use real absolute paths for execution. reference_window requires FFmpeg/ffprobe/Pillow; music_candidates requires FFmpeg/ffprobe/NumPy/SciPy. EveryFrame.jpg is evidence to inspect, not an automatic quality grade. Music JSON stores decoded-relative times and provisional requested-source times; reconcile the PTS origin before aligning a native sequence. A short audio excerpt is insufficient to establish whole-song tempo or arrangement.

## Musical evidence

- Extract the actual music used, including edits/source offset. Account for audio/video start times and encoder delay. Evaluate the final rendered audio when checking delivery sync.
- Separate low-band percussive attack candidates, higher percussive attacks, broad onsets and energy envelope. Useful exploratory bands: kick 35–160 Hz, broader bass 30–200 Hz, snare-like 600–6000 Hz. These are estimates, not instrument stem isolation.
- Distorted bass, vocal consonants, effects and guitars can trigger these bands. Keep HPSS/FFT window size, hop and timing uncertainty with results. Do not interpret a 4 ms numeric difference as 4 ms perceptual accuracy.
- Test half/double-time hypotheses. Autocorrelation maxima are candidates. Confirm pulse and phrase starts by listening; fit beat phase and local drift rather than rounding the whole song to one BPM.
- Mark phrase change, break, build, vocal entry, attack and release independently. Do not cut every detected peak or retain a bass grid through a bass-free passage.
- Repeated lyrics do not guarantee identical musical lead-ins. The JUMP study finds similar ASR count cues near 31 and 97 s, but different subsequent energy patterns; inspect each occurrence before copying the same transition timing.
- For each visual accent, record measured signed delta to the relevant *verified* attack. Keep detected peak, perceived attack, edit point and action contact as four separate fields.

## Reference annotation record

Use one row per purposeful event:

`reference_id, fingerprint, source_pts_start/end, source_fps, coverage_level, event_type, visible_action, shot_size, attention_position, motion_in/out, palette, musical_event_time/type, audio_verification, lyric_function, lyric_verification, observed_fact, interpretation, alternative_explanation, transfer_to_current_subject, confidence, evidence_path`

Observe first. Example: a graphic palette swap lasts four source frames and the same face returns. Possible interpretation: a short identity accent. Alternative: stylized performance continuity. Do not write "the director intended X" from pixels alone.

## Practical adaptation

Transfer the relationship, not the fictional props. Weapon discharge can become ball contact, boxing contact, trampoline landing or a slide arrival. Preserve preparation, payoff and recovery. A joyful venue piece should not import the reference's fear, injury or despair merely because the frames look cinematic.

Plan tension across phrases: establish subject -> preparation -> energy burst -> payoff -> readable reaction. Let camera motion carry some beats. Use motifs with recurrence and change, not unrelated stock graphics.

Before building a complex effect, make a 1–3 s study with the real subject. Judge silhouette, eye line, edge quality and visual return to the footage. A generic card, pill-shaped crop or heavy edge wash is not justified by a reference containing sophisticated compositing.

## Production prompt template

"Use $gmv-edit. Read the live brief and current coverage ledger. Project/native app: [...]. Allowed raw source roots: [...]. Protected timeline/audio ranges: [...]. Exclusions and repeat-person limits: [...]. Delivery aspect/FPS: [...]. Music file and exact edit/source mapping: [...]. Reference ID + inspected time windows: [...]. Borrow these observed relationships: [...]. Graphics allowed: [...]. For each chosen action, log preparation/contact/recovery and the target musical event. Produce a shot/action map and one representative effect study before the full build. Keep source clips editable. Verify music, action and cut timing separately; inspect the actual native export and do not restore user-deleted ranges. Report viewed vs inferred vs pending evidence."

## Research continuation

Save inventory, fingerprints, coverage ledger, observed examples, tool versions, errors, active process IDs, completed outputs and exact next commands. Check new files incrementally. A scheduled continuation is not a quota-reset event and cannot guarantee execution while the app/host or account quota is unavailable. Use the automation supported and explicitly requested in the current session.
