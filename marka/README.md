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

## Marka Kimliği Rehberi (v2.0)

```bash
python3 marka/kimlik_pdf.py   # marka/kimlik.html
# sonra Chromium ile A2 yatay PDF'e basılır
```

11 sayfa, 594×420 mm. Müşterinin v1 dosyasının yapısı korundu; fark
mockup'larda: düz vektör ikon yerine gölge katmanları, yüzey gradyanları,
kağıt/kumaş dokusu (SVG `feTurbulence`) ve perspektif kullanıldı.

| | |
|---|---|
| 01 | Kapak |
| 02 | Logo yapısı ve kilit versiyonları |
| 03 | Bakır Bronz paleti + zemin kombinasyonları |
| 04 | Yazı ailesi + ölçek merdiveni |
| 05 | Zarf · Antet · Kartvizit |
| 06 | Tabela · Tiny House |
| 07 | Tişört · Şapka |
| 08 | Kupa · Suluk · Anahtarlık |
| 09 | Sosyal medya · Web sitesi |
| 10 | Koruma alanı · En küçük ölçü · Yapılmaz |
| 11 | Kapanış |

### v1'e göre değişenler
- Çatı kısaltıldı (`TEPE = 70`) — amblem daha yatay, daha oturmuş
- Kilit içinde amblem küçültüldü; logotype ile dengesi düzeltildi
- Tüm mockup'lar gerçekçi hacim ve malzeme hissiyle yeniden çizildi
- Yeni sayfa: koruma alanı, en küçük ölçü ve yapılmaz kuralları

## Teslim seti

`marka/teslim/` — dikey, yatay, amblem, negatif, tek renk.
Kilit dosyalarındaki yazı hâlâ canlı metin; **baskıya gitmeden önce
outline'a çevrilmeli** (amblem zaten saf vektör).
