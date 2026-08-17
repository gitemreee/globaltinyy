# Ürün ve Hizmet Kataloğu

Kaynak: `katalog.html` (tek dosya, A4 baskıya göre kurgulanmış).
Görseller: `img/` — `public/images/` içindeki webp'lerden 1200px JPEG olarak türetilir.

## PDF üretmek

```bash
npm run katalog
```

Çıktı: `katalog/Global-Katalog-2026.pdf` (git'e girmez).

## Fotoğraf eklemek

Kataloğda kesikli çerçeveyle işaretli **GÖRSEL ALANI** kutuları, henüz fotoğrafı
olmayan bölümleri gösterir (otel mobilyası, gardırop/TV ünitesi, ofis düzenleme).
Yeni fotoğraf geldiğinde:

1. Fotoğrafı `katalog/img/` içine koy (max 1200px genişlik, JPEG).
2. `katalog.html` içinde ilgili `<div class="ph">…</div>` bloğunu
   `<figure style="height:XXmm"><img src="img/dosya.jpg" alt=""></figure>` ile değiştir.
3. `npm run katalog` çalıştır.

## Sayfa düzeni

01 Kapak · 02 İçindekiler · 03 Biz Kimiz · 04 Faaliyet Alanları ·
05 Ayraç A · 06 Tiny House · 07 İç Mekân · 08 Kiosk & Coffee ·
09 Karavan · 10 Özel Projeler · 11 Ayraç B · 12 Otel Mobilyası ·
13 Ev Mobilyası · 14 Ofis & İş Yeri · 15 Üretim ve Malzeme ·
16 Süreç · 17 Teslimat ve Garanti · 18 SSS · 19 İletişim
