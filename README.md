# GlobalTinyy

Global Investment Yapı Geliştirme A.Ş. için 17 sayfalık, bağımlılıksız statik site.
Kaynak `data/` + `src/`, çıktı `dist/`. Tek komutla hem **Netlify** hem **GitHub Pages** için üretilir.

| | |
|---|---|
| Repo | https://github.com/gitemreee/globaltinyy |
| Netlify | https://globalyapicelik.net |
| GitHub Pages | https://gitemreee.github.io/globaltinyy |

## Yapı

```
data/site.json       Marka bilgileri + platform hedefleri (siteUrl / basePath)
data/pages.json      17 sayfanın içerik ve SEO verisi
src/styles.css       Tek dosya CSS
public/images/       Görseller (webp)
scripts/config.mjs   Hedef/URL/basePath çözümü
scripts/build.mjs    dist/ üretir
scripts/serve.mjs    Lokal önizleme sunucusu
netlify.toml         Netlify build + header ayarları
.github/workflows/   GitHub Pages deploy workflow'u
```

`dist/` git'e girmez; iki platform da kendi build adımında üretir.

## İki platform, tek kaynak

Fark iki değerde toplanır ve `data/site.json` içindeki `targets` bloğundan gelir:

| | Netlify | GitHub Pages |
|---|---|---|
| `basePath` | `/` | `/globaltinyy/` |
| `siteUrl` | `https://globalyapicelik.net` | `https://gitemreee.github.io/globaltinyy` |
| İletişim formu | Netlify Forms (`teklif`) | JS demo (gönderim yok) |

Hedef `DEPLOY_TARGET` ile seçilir (`netlify` | `pages`). Verilmezse Netlify ortamı
otomatik algılanır (`NETLIFY` değişkeni), aksi halde `pages` kullanılır.

`SITE_URL` ve `BASE_PATH` değişkenleri hedefteki değerleri ezer. Netlify build'inde
`URL` değişkeni otomatik geldiği için canonical adresler özel alan adına geçtiğinizde
kendiliğinden güncellenir — `site.json`'u elle düzenlemeye gerek kalmaz.

## Geliştirme

```bash
npm run dev            # Pages yolu ile: http://localhost:4173/globaltinyy/
npm run dev:netlify    # Netlify yolu ile: http://localhost:4173/
```

Her ikisi de önce build alır. Port `PORT` ile değiştirilebilir.

## Build

```bash
npm run build          # ortamdan algılar
npm run build:netlify  # DEPLOY_TARGET=netlify
npm run build:pages    # DEPLOY_TARGET=pages
```

## Deploy

**Netlify** — `netlify.toml` hazır: build `npm run build`, publish `dist`,
`DEPLOY_TARGET=netlify`, Node 22. Repo'yu Netlify projesine bağlamak yeterli;
`main` push'u deploy tetikler. Manuel deploy için:

```bash
netlify deploy --prod
```

**GitHub Pages** — Settings → Pages → Source: **GitHub Actions**.
`main`/`master` push'unda workflow build alıp yayınlar.

Aynı repo iki yere birden deploy edilebilir; çıktılar hedefe göre farklı üretildiği
için yollar ve canonical adresler çakışmaz.

## İletişim formu (Netlify)

Netlify build'inde form `data-netlify="true"` ile üretilir; gönderimler Netlify
panelinde **Forms → teklif** altında görünür. Başarılı gönderim `/tesekkurler/`
sayfasına yönlenir. `bot-field` honeypot'u spam'i filtreler.
Bildirim e-postası için: Netlify → Project configuration → Forms → Form notifications.

## SEO

Her sayfada özel title/description, canonical, Open Graph, JSON-LD WebPage verisi;
`sitemap.xml`, `robots.txt` ve `404.html` build sırasında hedefin adresine göre üretilir.
Deploy preview ve branch deploy'ları `X-Robots-Tag: noindex` ile indekslenmeye kapalıdır.

## Renk paleti

`#ADFCF9` · `#89A894` · `#4B644A` · `#49393B` · `#341C1C`
