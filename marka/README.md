# Marka · GLOBAL YAPI GELİŞTİRME A.Ş.

## Logo

Harfler fontla dizilmez — `logo.py` içinde geometrik olarak çizilir (monoline sans).
Marka fikri iki mimari detayda:

- **A** → çatı. Orta kiriş iki yana taşarak saçak olur.
- **O** → dörtlü pencere kayıtları. Aynı zamanda meridyen/ekvator iması verir;
  kasıtlı olarak sade tutuldu (yoğun bir dünya çizimi göz yorar).

```bash
python3 marka/logo.py     # marka/svg/*.svg üretir
```

### Parametreler
| | |
|---|---|
| `w` | ana çizgi kalınlığı |
| `track` | harf arası boşluk |
| `thin_ratio` | ikincil (pencere kaydı) çizgi oranı |
| `cati` | `kiris` (taşan orta çubuk) veya `sacak` (ayrı ince çizgi) |
| `KERN` | optik kerning tablosu — yuvarlak/köşegen harf düzeltmeleri |

## Durum

Konsept aşaması. Karar bekleyen: çatı varyantı ve ağırlık.
Seçim kesinleşince tipografi ve renk paleti buna göre kilitlenip
kataloglara entegre edilecek.

Açıklama satırı (`YAPI GELİŞTİRME A.Ş.`) şu an sistem fontuyla diziliyor;
final pakette outline'a çevrilmeli.

## Onaylanan yön (v3)

| | |
|---|---|
| Ağırlık | K2 orta — çizgi 13, tracking 28 |
| A | Saf çatı, yatay çubuk yok |
| O | Sade daire (pencere kayıtları wordmark'ta kullanılmıyor) |
| Amblem | Cephe — çatı + dörtlü pencere |

Pencere kaydı fikri wordmark'tan çıkarıldı, amblemde yaşıyor.
Böylece kelime sakin kalıyor, işaret anlatıyor.

### Dosyalar (`marka/svg/`)

```
logo-yatay-{siyah,beyaz,greige}.svg    ana kullanım
logo-dikey-{...}.svg                   kare alanlar
wordmark-{...}.svg                     açıklama satırı olmadan
amblem-cephe-{...}.svg                 ana amblem
amblem-{pencere,cati}-{...}.svg        alternatifler
favicon.svg                            kalınlaştırılmış, 16-32 px için
```

Ölçek sınırı: yatay kilit en az 25 mm / 110 px genişlikte kullanılmalı.
Daha küçükte amblem kullanılır.
