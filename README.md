# Global Yapı Geliştirme A.Ş.

Tiny house, ölçüye özel mobilya ve karavan üretimi yapan firmanın kurumsal sitesi.
Statik site — `data/icerik.json` + `src/` → `dist/`.

| | |
|---|---|
| Canlı | https://globalyapicelik.net |
| Repo | https://github.com/gitemreee/globaltinyy |

## Yapı

```
data/icerik.json     Tüm site içeriği (kollar, seçenekler, süreç, rakamlar)
data/site.json       Marka + platform hedefleri (siteUrl / basePath)
src/styles.css       Tek dosya CSS, duyarlı
src/amblem.svg       marka/amblem.py çıktısı
public/images/       Proje fotoğrafları (webp)
scripts/build.mjs    dist/ üretir
scripts/config.mjs   Hedef/URL/basePath çözümü
marka/               Logo, amblem ve marka kimliği rehberi
katalog/             Tiny house ve mobilya katalogları (PDF)
```

## Sayfalar

`/` · `/tiny-house/` · `/mobilya/` · `/karavan/`
Ek olarak `404.html`, `sitemap.xml`, `robots.txt` ve Netlify'da `/tesekkurler/`.

Her kol sayfasında seçenek sekmeleri var (tiny house tipleri, mobilya alanları,
karavan çeşitleri). **Tüm paneller HTML'de basılıdır**, JS yalnızca gösterip gizler —
böylece arama motoru hepsini görür.

## Geliştirme

```bash
npm run dev            # Pages yolu:  http://localhost:4173/globaltinyy/
npm run dev:netlify    # Netlify yolu: http://localhost:4173/
npm run build          # ortamdan algılar
npm run katalog        # katalog PDF'lerini basar
```

`dist/` git'e girmez; iki platform da kendi build adımında üretir.

## İki platform, tek kaynak

| | Netlify | GitHub Pages |
|---|---|---|
| `basePath` | `/` | `/globaltinyy/` |
| `siteUrl` | globalyapicelik.net | gitemreee.github.io/globaltinyy |
| İletişim formu | Netlify Forms (`teklif`) | JS demo |

Hedef `DEPLOY_TARGET` ile seçilir; verilmezse Netlify ortamı otomatik algılanır.
`SITE_URL` / `BASE_PATH` değişkenleri hedefteki değerleri ezer.

## SEO

Sayfa başına özel title/description, canonical, Open Graph ve JSON-LD
(ana sayfada Organization + LocalBusiness, kol sayfalarında Service +
OfferCatalog). `sitemap.xml` ve `robots.txt` build'de hedefin adresine göre üretilir.

**Sırada:** çok dilli yapı (EN/FR/DE + hreflang), hizmet × şehir sayfaları,
Search Console doğrulaması ve GA4. GSC ve GA4 kodları hesaptan alınıp
`scripts/build.mjs` içindeki `<head>` bloğuna eklenecek.

## İçerik kaynağı

7 yıl deneyim · ~200 tamamlanmış iş · Köyüm Akmeşe'de 260 ünitelik aktif üretim.
Tiny house tipleri 1+0'dan 3+1 ve mega boya, ofis ve ticari konseptler.
Mobilya: ev (mutfak/yatak odası/banyo), ofis sabit, duvar kaplama, proje/otel.
Karavan: Karayolları şartnamesine uygun ticari, özel üretim yaşam karavanı.

Eksik: atölye adresi; otel ve ofis mobilyası referans fotoğrafları.
