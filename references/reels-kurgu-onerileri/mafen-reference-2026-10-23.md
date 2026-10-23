# MAFEN — Kullanıcının son finalinden gözlemler

İnceleme: 23 Ekim 2026. Bu kayıt, Reels Kurgu Önerileri alt modülündeki kararların somut örneklerini tutar; videonun bütünüyle kusursuz olduğuna dair bir onay değildir.

- Kaynak: `MAFEN - Final 1080x1920.mp4`
- Kimlik: SHA-256 `182e827ee8c82a993d05a8aa97a0cb4aec3fa1432a0bf1feb6b6dd3b4781fdd9`
- Ölçülen dosya: 1080 × 1920, 30 fps, 889 kare, yaklaşık 29,633 saniye.
- Görsel inceleme: tüm süreye yayılmış kareler; 7,35–8,70 ve 16,95–18,60 saniyede 0,15 saniye aralıklı yoğun örnekler; 15,14–16,36 ve 22,80–29,60 saniyede fotoğraf hareketi karşılaştırmaları.

## Gözlenen durum ve uygulanabilir karar

| Yaklaşık final zamanı | Görünen durum | Çıkarım / öneri |
| --- | --- | --- |
| 0,15–1,00 s | Kemer altından kameraya yürüyen kişi ve taşıdığı etkinlik tabelası birlikte okunuyor. | Açılış planında yüz, hareket ve işaret/tabela ilişkisini koruyan kadraj önemlidir. Bu karelerden hareketin ne kadarının kamera/özne veya dijital işlemlerden geldiği tek başına kesinleşmez. |
| 7,65–8,10 s | Soru işaretli kart, öğretmenlerin yüzleri ve öndeki renkli kartlar aynı çapraz kompozisyonda görülüyor. | Yalnızca yakınlığa göre seçim yapma; insan ve etkinlik nesnesini birlikte gösteren açı güçlü bir ana plan olabilir. |
| 15,14–16,36 s | Üç kişilik fotoğrafta kişiler büyüyor; odak grupta kalıyor. Önceki Rev03 çıktısında aynı fotoğraf yatay taranıyordu. | Kompakt ve uzaktaki grupta Scale yaklaşımı, gereksiz yatay taramaya göre odağı daha iyi koruyabilir. Bu tercih kullanıcı tarafından açıkça belirtilmiştir. |
| 17,10–17,55 s | Yazı yazan el, kalem ve masa ayrıntıları belirgin. | Eylem detayı amaçlandığında el/nesne kadrajı kullanılabilir; her planda tam vücut gösterme şartı koyma. |
| 17,70–18,60 s | Yapboz farklı yönlerden görülüyor. Bazı karelerde başların arkası baskın; 18,30–18,60 aralığında yan açı el, yüz profili ve oyun yüzeyini daha çok birlikte gösteriyor. | Kaynakta seçenek varsa etkinliği en rahat okutan açıya öncelik ver; diğer yönleri kısa bağlayıcı olarak değerlendirebilirsin. |
| 22,80–29,60 s | Geniş toplu fotoğraf soldan sağa taranarak farklı kişileri açığa çıkarıyor. | Yatayda yayılan grubun tamamını zaman içinde göstermek için Position taraması uygun olabilir; kompakt üçlü fotoğrafla aynı hareket reçetesine ihtiyaç duymaz. |

## Ölçüm sınırları

Üçlü fotoğrafın 15,14 ve 16,36 saniyedeki ihraç edilmiş kareleri arasında ORB eşleşmeleri ve sağlam 2B benzerlik dönüşümüyle yaklaşık **1,384 kat görünür ölçek artışı** tahmin edildi (600 aday eşleşme, 419 uyumlu nokta). Bu, yaklaşık görüntü değişimidir; native Scale alanının yüzde değeri, anchor point, easing eğrisi veya kullanılan uygulama kanıtı değildir. Yeni projelere yüzde reçetesi olarak taşınmaz.

Otomatik kare farkı eşiği çok sayıda aday verdi; kamera/özne hareketi de bu eşiği aşabildiği için aday sayısı kesme sayısı olarak kullanılmadı. Müzik ve algısal senkron bu incelemede dinlenerek doğrulanmadı. Kaynak dosya yalnızca okundu; yeni video renderı üretilmedi.

Bu depoda yalnızca metin gözlemleri bulunur; özel video, fotoğraflar ve yerel inceleme materyalleri paylaşılmaz. Aynı isimli başka bir dosyayı otomatik olarak bu referans sayma; kaynak kimliğini yukarıdaki hash ile doğrula.
