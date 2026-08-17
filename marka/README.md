# Marka · GLOBAL YAPI GELİŞTİRME A.Ş.

## Seçilen yön: ÇATI ÇİZGİSİ · endüstriyel ton

Fikir: çatı tek bir harfe sıkışmaz. Saçak **bütün kelimenin üstünden** geçer ve
**A'nın tam apeksinde** kırılır — yapı, markanın üstünü örter. Uçlardaki mertek
ayakları çatıyı kelimeye kilitler.

Amblem bu saçağın indirgenmiş hâli: **portal** — çatı + iki ayak.
Ayrı bir ikon icat edilmedi, logonun kendi parçası küçültüldü.

```bash
python3 marka/final.py     # marka/svg-final/*.svg
```

### Ölçüler
| | |
|---|---|
| Gövde çizgisi | 17 (cap 100'e göre) |
| Saçak çizgisi | gövdenin %72'si — uzun olduğu için ince olmalı |
| Tracking | 26 |
| Saçak tepe / saçak hizası | −76 / −32 |
| Kerning | `KERN` tablosu + kalın ağırlık düzeltmesi |

A crossbar'sızdır (saf çatı) — bilinçli karar.

## Reddedilen denemeler

- `logo.py` — v1/v3. Çatılı A + dörtlü pencere O. Amblem jenerikti
  (çatı+daire her inşaat firmasında var), wordmark imza taşımıyordu.
- `yonler.py` — v4. Üç alternatif; Y2 çatı çizgisi seçildi.

Arşiv olarak duruyor; üretim dosyası `final.py`.

## Sıradaki

Tipografi ve renk paleti seçilecek, sonra iki kataloğa entegre edilecek.
Açıklama satırı (`YAPI GELİŞTİRME A.Ş.`) şu an sistem fontuyla — final
pakette outline'a çevrilmeli.
