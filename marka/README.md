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
