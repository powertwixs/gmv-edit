# Sürüm notları

## Beta 0.1.1 — 23 Ekim 2026

Paket sürümü: `0.1.1-beta` · Git etiketi: `v0.1.1-beta`

### Yenilikler

- **Reels Kurgu Önerileri alt modülü:** GMV içinden gerektiğinde yüklenen etkinlik/marka Reels rehberi eklendi.
- **Fotoğrafa göre hareket:** küçük ve uzaktaki kompakt kişi/gruplarda odaklı Scale yakınlaşma veya uzaklaşma; yatayda geniş içerikte Position taraması. Sabit zoom yüzdeleri yerine özne, çözünürlük ve süreye göre karar verilir.
- **Kamera açısı seçimi:** yüz, el, nesne ve aksiyonu en iyi gösteren kaynak açıya öncelik; geniş/orta/detay/tepki çeşitliliği ve hareket boyunca kadraj kontrolü. Dijital crop gerçek yeni kamera açısı olarak sunulmaz.
- **Davul ve müzik girişi:** gerçek kick/trampet atakları, aksiyonun hazırlık/sonuç anları ve izin verilen kısa kesitlerde kesilip yeniden başlıyormuş hissi veren girişler için kontrol adımları eklendi.
- **Doğal, canlı renk:** çekim bazında pozlama, beyaz dengesi, kontrast ve canlılık eşleme; ten tonu, parlak alan ve gölge ayrıntısını koruma önerileri eklendi.
- **MAFEN örnek incelemesi:** zaman aralıklı metin gözlemleri, Scale/Position karşılaştırması ve ölçüm sınırları eklendi. Özel fotoğraf/video ve yerel kullanıcı yolları paylaşılmaz.

### Korunan ve netleştirilen davranış

- Kullanıcı süre veya müzik bölümü belirtmezse müziğin tamamı, özgün sıra ve hızında, kesintisiz kullanılır. Bu kural ilk Beta 0.1 etiketinden sonra ana dala eklenmişti; bu sürüme dahildir.
- Açık kısa süre/bölüm talebi ve korunan timeline aralıkları önceliklidir. Reels alt modülü otomatik 20/30 saniye sınırı getirmez.
- Orijinaller ve düzenlenebilir native proje/Scale/Position anahtarları korunur. Gözlem, kullanıcı tercihi ve öneri ayrı tutulur.

### Doğrulama ve kapsam

Ana skill ve alt modül yapısal doğrulayıcıyla, yeni yerel belge bağlantıları ve sürüm etiketleri kontrol edilmiştir. Bu sürüm talimat ve referans güncellemesidir; dört Python analiz aracında değişiklik yoktur. Yeni bir video renderı veya kesintisiz görsel/işitsel onay iddiası içermez.
