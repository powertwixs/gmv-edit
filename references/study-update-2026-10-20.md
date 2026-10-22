# Second research pass: new references and native proof

As of 2026-10-20: 25 references plus JUMP future music in the inventory. Their overviews and four dense sample windows per reference were inspected. Eight every-frame windows total were inspected. This is still not full audiovisual viewing. Runtime audio emission was tested and returned that direct audio input is unsupported; numerical/ASR work must remain labeled accordingly.

## Seven added reference samples

| Reference / source ID | Sample | Observed relationship |
|---|---|---|
| Arcane: Ekko and Jinx Team Up `B_KSH6w-gps` | 2.542–2.958; 47.750–48.167 | Face/face dialogue cut differs from the later movement/green projectile bridge. Do not borrow dialogue timing as proof of beat timing |
| BRING IT ALL / IN MY ZONE `WyYiVdNhTE0` | 63.167–63.583 | Action/energy facing camera -> readable surprised reaction; preserve the reaction's purpose |
| GIVE THEM NOTHING / Veto `2FLY-gn-hGQ` | 57.375–58.333, every frame | Cyan fist with black trailing shape; monochrome textured extension at 57.750; ink whorl at 57.792/57.833; hand opens by 57.875 and cyan returns at 57.917. One drawing evolves through forms, carrying direction and silhouette |
| INCURSIONS `6nKzziP2lxw` | 68.292–68.708 | Group looking at bright display -> one face reaction; focus narrows from group task to individual response |
| NEVER FIGHT ALONE / Miks `gictwC-KlTk` | 54.583–55.542, every frame | Cropped console/body action through 55.000; white silhouette on black at 55.041667/55.083333; inverted dark silhouette on pale field at 55.125/55.166667; live environment returns at 55.208333. Four-frame insert preserves a pose/action through a graphic inversion |
| VOCÊ É BRABA / Game Changers `69sKYwsxUM8` | 34.000–34.767, every frame, 30 fps | Side profile develops expanded cyan hair/silhouette, a broad graphic smear at 34.400, an enlarged head form at 34.500, then whole upper body action at 34.600. Held and changed drawings create cadence inside one shot; do not count each drawing as a new camera cut |
| WHY WE FIGHT BACK `AnGdzz-XWcE` | 154.667–155.083 | Green character/hand energy becomes a blue projectile close detail; origin and direction motivate the detail cut |

The previous first-pass note called `AfcCyTsh4ag` PUSH based on a visible card. The actual supplied filename identifies RISE AND FALL / Hush Agent Trailer. Use the inventory title, and keep observed on-screen text separate from film identity.

## Lyrics and intent: provisional cross-modal readings

The following use unverified singing ASR. They are hypotheses to check, not established lyric synchronization or creator intent:

- GODS around 40–43 s: an ASR identity/power refrain overlaps a large environment/light change. Possible reading: scale and stakes; an alternative is simply a phrase-boundary visual payoff.
- RISE around 107–111 s: an ASR recognition/ascent refrain overlaps warm action and a cool impact flash. Possible reading: effort culminating in a payoff; the visual hit itself does not prove a word-specific cue.
- Wasteland around 42–46 s: a bleak-world phrase candidate overlaps a weapon discharge. This could be emotional contrast rather than literal illustration. Do not copy the violent/despairing tone into a cheerful venue film.
- WHY WE FIGHT around 146–151 s: a breathing/release phrase candidate overlaps a large group/bright environment followed by intimate microphone detail. Possible reading: shifting from collective stakes to personal voice. ASR timing needs checking.
- PARANOIA around 22.4 s has no overlapping segment in the current ASR output. This absence does not prove an instrumental passage; it prevents asserting a specific word-driven graphic cue.

## Verified local native workflow

AE 26.5x89 in an independently launched empty process built and rendered `native_study_01/GMV_Native_Motion_Study.aep` in the research workspace. Two original editable Shape studies, each 1080x1920, 120 fps, 1.2 s, 144 native frames: contact burst and directional strokes. These simple procedural assets establish tool execution, layer editability and alpha output; they do not reproduce the references' character animation or completed live-action compositing.

Isolation used an inherited per-launch token plus a pristine/empty-project guard. The current open Adobe projects were not used. Direct CLI ExtendScript lacked JSON; self-contained serialization was necessary. The actual output templates did not contain PNG Sequence; TIFF Sequence with Alpha was available. Its Channels setting was read-only, so the alpha template was used directly.

Before reusing the rendered assets, read their QA record: TIFF has four samples but ExtraSamples=0, so Pillow displays RGB and discards the fourth sample by default. Inspect actual sample bytes/FFmpeg decode rather than declaring alpha missing from a Pillow mode check. ProRes 4444 derivatives were encoded at explicit 120 fps; image-sequence ingest must not default to 25 fps.

## Current limits and next work

The two assets are simple technical studies. Next, make an isolated native *real footage* test of pose-preserving matte plus registered drawing, with original-resolution edges, intentional entry/return and source action timing. Do not present the simple rays as equivalent to complex paint/character work. Select non-flash passages for broader narrative analysis. Direct perceptual listening remains unverified; do not loop forever claiming it is about to happen in a runtime without audio input.
