# GMV Edit — Beta 0.1.2

Release: **Beta 0.1.2** (`0.1.2-beta`).

An open-source agent skill for music-led game music videos, live-action Reels and reference-driven footage editing. It combines bass/action timing, shot continuity, original drawn accents and editable Adobe workflows.

This is a skill with instructions and analysis helpers, not a trained model, Adobe plugin or automatic one-click video editor.

## Beta 0.1.2 yenilikleri

- [Etkinlik Reels akışı](references/event-reels-workflow.md): tam konuşma, J/L cut, kesintisiz fon, hareketli çift/grup kadrajı ve taslak sonrası düzeltme.
- [Kopyalanabilir Türkçe brief](references/event-reels-handoff.md): Antigravity veya başka bir kurgu ajanına güncel kaynak, süre ve teslim koşullarını aktarmak için.
- Kaydedilmiş Premiere dosyasından bağımsız doğrulama; stereo stem, HDR/Rec.709, Motion ve yinelenen Lumetri özellik adları için [native notlar](references/adobe-notes.md).
- Güncel revizyonu esas alma ve manuel düzeltmeleri son plana işleme; eski oluşturucuyla reddedilmiş seçimleri geri getirmeme.

## Beta 0.1.1 ile gelenler

- [Reels Kurgu Önerileri](references/reels-kurgu-onerileri/SKILL.md): etkinlik/marka videolarında kamera açısı, dijital kadraj, fotoğraf hareketi, ritim ve doğal renk rehberi.
- Küçük ve uzaktaki kompakt öznelerde odaklı Scale yakınlaşma/uzaklaşma; yatayda yayılan içerikte Position taraması. Hareket her fotoğrafın yapısına göre seçilir.
- En iyi gerçek çekim açısını seçme; geniş/orta/detay/tepki çeşitliliği ve hareket boyunca kadraj kontrolü.
- Gerçek kick/trampet ataklarını dikkate alma, izin verilen kısa müzik kesitlerinde durup yeniden başlıyormuş hissini kontrol etme ve çekim bazında doğal, canlı renk eşleme.
- Metin tabanlı MAFEN inceleme örneği ve açık kanıt sınırları. Özel medya pakete dahil değildir.

Süre belirtilmezse **tam ve kesintisiz müzik** varsayılanı korunur; kullanıcının açık kısa süre/bölüm talebi önceliklidir. Ayrıntılar: [sürüm notları](CHANGELOG.md).

## What it does

- Breaks down reference passages with source timestamps and explicit review coverage.
- Keeps musical attacks, camera cuts, action contacts and graphic accents separate.
- Plans readable preparation/action/reaction sequences instead of cutting at every detected peak.
- Provides Premiere Pro and After Effects recipes for retiming, pose mattes, tracked strokes, brush forms, alpha exports and audio alignment.
- Preserves original media, protected timeline regions and editable native projects.
- Distinguishes observations, creative interpretations, unverified lyrics and actual rendered proof.

## Install

Clone this repository as `gmv-edit` inside your agent's skill directory. For a user-scoped Codex installation using the default directory:

```powershell
git clone https://github.com/powertwixs/gmv-edit.git "$env:USERPROFILE\.codex\skills\gmv-edit"
```

If `CODEX_HOME` is configured, use its `skills/gmv-edit` directory instead. Keep any existing local version; do not overwrite it blindly. Other skill-compatible agents can use the same `SKILL.md` folder layout according to their installation instructions.

The structure follows the [official OpenAI skills guide](https://developers.openai.com/plugins/build/skills). The [official Codex workflow example](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) documents the default user-scoped skill directory.

## Use

**Default duration:** if you do not specify a shorter length or music range, edit the entire supplied track from start to finish and keep the music uncut. Short reference windows, effect tests and a request to evaluate the skill do not impose a short-video limit.

```text
Use $gmv-edit to create a mixed-game GMV from the supplied game footage.
Music: [...]. References and passages: [...].
Delivery aspect/FPS/duration: [...]. Editable application: [...].
Protected ranges, exclusions and allowed graphics: [...].
Inspect the sources, map preparation/action/reaction to the music,
and verify the actual native export before calling it finished.
```

For a live-action promo, specify the allowed camera footage and venue instead. Event/brand Reels with footage and photos load the Reels submodule through the parent skill; set a short duration explicitly when required. A new independent game GMV must not silently reuse an unrelated client edit.

## Optional Python tools

Instructions can be used without Python. The analysis helpers need Python 3.10+; media extraction also needs `ffmpeg` and `ffprobe` on PATH. Install Python dependencies explicitly if you want the helpers:

```powershell
python -m pip install -r requirements.txt
python scripts/reference_window.py "reference.mp4" --start 22.3 --frames 24 --output "analysis/frames-01"
python scripts/music_candidates.py "music.mp4" --start 32 --duration 8 --output "analysis/music-01"
python scripts/check_action_anchors.py "plan.json"
python scripts/region_continuity.py "regions.json" --output "analysis/regions-01"
```

| Helper | Output / limit |
|---|---|
| `reference_window.py` | Consecutive frames, actual source PTS, contact sheet; no automatic shot classification |
| `music_candidates.py` | Provisional low/high percussive attacks and tempo candidates; no verified listening or lyrics |
| `check_action_anchors.py` | Frame coverage, source-time arithmetic and sampling warnings; no visual rhythm judgment |
| `region_continuity.py` | Manually annotated region/color proxies; no gaze tracking or automatic grading |

Plan schemas are in [action anchors](references/action-anchor-workflow.md) and [color/attention](references/color-attention-study.md). Use a new analysis output folder. Sources remain read-only. Generated JSON reports contain your local input paths; review them before sharing.

## Evidence and limitations

Historical study notes preserve measured examples, rejected attempts and known Adobe version differences. The private lab's evidence media, original footage, native client projects and rendered assets are not part of this repository. Reproduce checks with your own authorized media. A contact sheet is not uninterrupted audiovisual review; acoustic candidates are not verified lyrics or proof of creator intent. A 120 fps graphic render does not create new captured motion in a 24/30 fps source.

## Türkçe

GMV kurgusu için geliştirdiğimiz yöntemleri, referans inceleme notlarını ve dört analiz aracını içerir. Müziğin bas vuruşu, sahne kesimi, görüntüdeki aksiyon ve çizim efektini ayrı ayrı değerlendirir. Ham dosyaları ve düzenlenebilir projeleri korur. Özel çekimler, müşteri profilleri ve medya dosyaları paylaşılmaz.

## License and media

The original skill text and helper scripts in this repository are available under the [MIT License](LICENSE). Third-party names and reference IDs identify analyzed works; no reference video, music, frame, logo or proprietary Adobe asset is included or licensed by this project. Adobe software and any optional third-party tools require their own installation and licenses. This is an independent project, not an official OpenAI, Adobe or game-publisher product.
