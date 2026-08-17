# Marka · GLOBAL YAPI GELİŞTİRME A.Ş.

Onaylı logo müşteriden geldi (PDF). `amblem.py` bu amblemi ölçerek
vektöre çevirir — çatı yüksekliği parametrik olsun diye.

```bash
python3 marka/amblem.py     # marka/svg-marka/*.svg
```

## Amblem

"G" harfi bir ev kesitiyle birleşir: sol duvar + taban G'nin gövdesi,
ortadaki yatay çubuk G'nin kirişi, bakır parçalar vurgu.

| Parametre | |
|---|---|
| `tepe` | çatı tepesinin y'si. 0 = orijinal; büyüdükçe çatı aşağı kısalır |
| `KAL` | şerit kalınlığı (75) |
| etek | 299 — sabit, çatı kısalırken duvar kotu değişmez |

Çatı kısalınca eğim değişir; şerit kalınlığı eğime dik ölçülüp dikey
izdüşümü yeniden hesaplanır (`boy / apex_x`), yoksa çatı incelir.

## Renkler (kimlik dosyasından)

| | | |
|---|---|---|
| Ana renk | `#2F3336` | amblem, logotype, koyu zeminler |
| Bakır bronz | `#B87333` | vurgu — PANTONE 876 C / RAL 8001 |
| Nötr gri | `#A6A39A` | ikincil metin, ayraçlar |
| Kağıt | `#F5F3F0` | zemin |

Oran: koyu %60 · kağıt %25 · bronz %10 · nötr %5. Bronz her zaman vurgudur.

## Yazı ailesi

Questrial (logotype + başlık) · Inter (metin) · IBM Plex Mono (teknik).

## Arşiv

`logo.py`, `yonler.py`, `final.py`, `kimlik.py` — müşteri logosu gelmeden
önceki denemeler. Üretimde kullanılmıyor.
