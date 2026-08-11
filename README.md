# Global Yapı Çelik

Çelik konstrüksiyon tiny house / prefabrik yapı sitesi. Statik site — build adımı yok.

| | |
|---|---|
| Repo | https://github.com/gitemreee/globaltinyy |
| Netlify | https://app.netlify.com/projects/globaltinyhouse |
| Canlı | https://globaltinyhouse.netlify.app |

## Yapı

```
index.html          Ana sayfa
netlify.toml        Netlify ayarları (publish = ".", güvenlik header'ları)
robots.txt
assets/css/styles.css
assets/js/main.js
```

## Telefondan çalışma

`main` branch'e her push otomatik deploy tetikler. Telefondan iki yol:

1. **github.dev** — Repo sayfasında `.` tuşuna bas (veya URL'de `github.com` yerine `github.dev` yaz). Tarayıcıda tam VS Code açılır, düzenle → commit → push.
2. **GitHub mobil uygulaması** — Dosyaya gir, kalem ikonu, düzenle, commit.

Push'tan ~30 saniye sonra canlı sitede görünür. Deploy durumu Netlify panelinden takip edilir.

## Bilgisayardan çalışma

```bash
netlify dev
```

Lokal sunucu açar (varsayılan http://localhost:8888), netlify.toml kurallarını uygular.

Manuel deploy (repo'ya dokunmadan):

```bash
netlify deploy --prod
```
