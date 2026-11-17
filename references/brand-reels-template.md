# Onaylı Reel için marka şablonu

## Onaylı videonun üzerine çalış

- Fiyat gizleme veya marka katmanı ekleme isteniyorsa onaylı sequence'i çoğalt. Onaylı sürüm yalnız video olarak geldiyse onu taban katman olarak kullan. Süreyi, kare hızını, kesmeleri, kaynak aralıklarını ve ses yerleşimini tabana göre koru.
- Fiyat görünürlüğünü çekim çekim kontrol et. Hareketli etikette maskeyi izle veya anahtar karelerle düzelt. Maske kenarının fiyatı açığa çıkardığı giriş, çıkış, hareket bulanıklığı ve kesme civarındaki kareleri çıktı çözünürlüğünde incele. Yazının okunabilirliğini ve komşu ürün detayını birlikte kontrol et.
- Kullanıcının seçtiği logo dosyasını kaynak al ve yerleştirilen asset'i kaydet. Video için küçültülmüş bir kopya gerekiyorsa özgün dosyayı ayrıca koru. Alt imzayı platform arayüzü ve görüntüdeki metinlerle birlikte kontrol et.

## İmzayı ve kapanışı yeniden kullanılabilir yap

- Sabit alt imzayı saydam PNG, animasyonlu kapanışı hedef editörün alfa destekli formatında teslim et. ProRes 4444 MOV, desteklenen Adobe iş akışlarında bir seçenektir. İmzanın kapanışta ne zaman kalkacağını ve varsa kapanışın son plan üzerine nasıl oturacağını belirle. Kapanış süresini brief'e göre ayarla.
- Düzenlenebilir projede logo katmanlarını, hareket anahtarlarını ve kapanış efektlerini ayrı tut. Alfa video üstteki renk ve saydamlığı taşır. Alttaki görüntüyü bulanıklaştırmak gerekiyorsa adjustment layer'ı ana kompozisyonda tut veya efekti kurgu uygulamasında uygula.
- Yeni videoda kapanışın başlangıcını yeni bitiş karesine göre yerleştir. Seçilen kapanış süresi toplam videoya sığmıyorsa animasyon ve yerleşimi yeniden ayarla.

## Teslimi kontrol et

- Kaydedilen projeyi yeniden açıp logo kaynağını, bağlı medyayı ve expression durumunu kontrol et. Ayrı alfa MOV'u hedef editörde görüntü üzerine yerleştir. Saydamlığı, ilk ve son kareyi, kapanış süresini ve imzadan kapanışa geçişi incele.
- Dışa aktarılan videonun kare sayısını, zaman tabanını ve ses senkronunu onaylı sürümle karşılaştır. Ses akışı doğrudan kopyalandıysa kaynak ve teslim ses akışlarının SHA-256 özetlerini karşılaştır. Ses yeniden kodlandıysa başlangıç ve bitişi, zaman hizasını ve duyulabilir farkları kontrol et. Dosyanın tamamını decode etmek, maskenin her kritik karede fiyatı gizlediğini tek başına göstermez.
