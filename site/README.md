# Site tasarımı — tasarım tuvali kaynakları

Marka kimliğine (bakır bronz paleti, Questrial/Inter/IBM Plex Mono, amblem)
göre kurulan site tasarımı. Her `.dc.html` bir tuval yüzeyi.

| Dosya | |
|---|---|
| `Main.dc.html` | Ana sayfa |
| `TinyHouse.dc.html` | Tiny house — tip seçici çalışır |
| `Mobilya.dc.html` | Mobilya — alan sekmeleri çalışır |
| `Karavan.dc.html` | Karavan — çeşit sekmeleri çalışır |
| `Mobil.dc.html` | Mobil ana sayfa — menü açılır/kapanır |
| `canvas.json` | Yerleşim, başlıklar, notlar |
| `amblem.svg` | `marka/amblem.py` çıktısı (tepe=70) |

Görseller `public/images/` arşivinden 620–720 px JPEG olarak türetildi
(tuval her kaydetmede tüm belgeyi yeniden yayınladığı için dosya başına
70 KB sınırı var).

**Amblem notu:** SVG kendi `width`/`height` değerlerini taşır; her kullanım
yerinde `style="height:…px;width:auto"` verilmezse doğal boyutunda (810 px)
render olur.

## İçerik kaynağı

Rakamlar ve kapsam müşteriden: 7 yıl, ~200 tamamlanmış iş, Köyüm Akmeşe'de
260 ünitelik aktif üretim; tiny house tipleri (1+0 → 3+1, mega boy, özel
konsept, ofis, ticari); mobilya alanları (ev, ofis sabit, duvar kaplama,
proje/otel); karavan (Karayolları şartnamesine uygun ticari, özel yaşam).

Doldurulmayı bekleyen: atölye adresi.
