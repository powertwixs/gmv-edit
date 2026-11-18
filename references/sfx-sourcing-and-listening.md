# SFX sourcing and listening for GMV Edit

Use this workflow when the current edit calls for sound effects, recorded sound sourcing, or an audio review. Do not add effects by default: the brief and GMV Edit's protected-audio and full-track rules take priority. Preserve editable source and audio tracks in the requested native application.

## Source and verify

1. Start with the user's authorized library and sounds already in the project. For real recorded SFX, read the installed `real-sfx/SKILL.md` under `CODEX_HOME/skills` (normally `~/.codex/skills`) and run its setup check before relying on its scripts. Report missing libraries or packages; do not invent available assets. Its UI pack and Earshot's sound bank contain synthesized sounds: do not substitute them when the brief requires recordings or prohibits synthesis.
2. When an openly licensed source is useful, search Openverse audio at `https://api.openverse.org/v1/audio/?q=whoosh&page_size=10`, replacing the query with the desired sound. Search English variants as needed. It is a catalog, not a license guarantee. Check the current original source page and license for each selected sound, including commercial use, adaptations, attribution and other restrictions; avoid incompatible or uncertain licenses. Save title, creator, source page, license and license URL with the project. The returned media URL may be a preview or unavailable; verify the actual usable file and its quality.
3. With Earshot MCP available, use `rank` for candidates and `find` for useful segments, then `describe` and, if real-recording character matters, `realness`. These are model assessments, not proof of provenance or a substitute for human audition. If unavailable, report the limitation and use available measurement and audition methods. Never claim human listening from an analysis alone.

## Place and review

Create a cue list tied to visible actions and the actual music; use restraint and preserve speech, existing music, protected regions and the user's editable timeline. For selected effects, check onset/peak against the intended action and compare the mix against the original. Use Earshot `timeline`, `sheet`, `ab` and `measure` as appropriate; confirm the final render's audio continuity, clipping and synchronization. Its launch-film critique profile is a reference, not an automatic standard for GMV or event edits. Only upload audio to an external audio-LLM when the user explicitly agrees.

If using Real SFX's rendered MP4/WAV workflow, treat it as a review or an extra deliverable when appropriate, not a replacement for the user's requested editable Premiere/AE project. Real SFX's project-specific examples, automatic ducking and source-removal suggestions do not override this project's instructions or authorization. Keep asset/license records and separate editable SFX tracks with the project.

