# Kataloglar

İki ayrı katalog, ortak tasarım sistemi:

| Dosya | Çıktı | Kapsam |
|---|---|---|
| `tiny-house.html` | Global-TinyHouse-Moduler-Yapilar.pdf | Tiny house, kiosk & coffee kiosk, karavan |
| `mobilya.html` | Global-Ic-Mekan-Ahsap-Mobilya.pdf | Mutfak, depolama, otel, ofis & iş yeri |

Her ikisi de 10 sayfa, A4. Ortak stil: `base.css`.
Görseller: `img/` — `public/images/` içindeki webp'lerden 1200px JPEG türevleri.

## PDF üretmek

```bash
npm run katalog        # ikisini birden basar
```

## Tasarım dili

Greige (`--tan`) + beyaz + antrasit (`--char`). Başlıklar iki parçalı:
solid kelime + hayalet (ghost) kelime. İnce çizgiler, 01/02/03 numaralı
kutular, bol boşluk.

**Başlık yazarken:** kelimeyi ortadan bölme. "Mut/fak" değil,
"Ölçüye Özel / Mutfak" gibi anlamlı iki parça kullan.

## Fotoğraf eklemek

Kesikli çerçeveli **GÖRSEL ALANI** kutuları henüz fotoğrafı olmayan
bölümleri gösterir (otel odası, lobi, gardırop, ofis düzenleme/mağaza).

1. Fotoğrafı `katalog/img/` içine koy (max 1200px genişlik, JPEG).
2. İlgili `<div class="ph">…</div>` bloğunu şununla değiştir:
   `<figure style="height:XXmm"><img src="img/dosya.jpg" alt=""></figure>`
   — `figure`'e yüksekliği **doğrudan** ver, parent'tan miras bırakma.
3. `npm run katalog`
