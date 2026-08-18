import fs from 'node:fs';
import path from 'node:path';
import { site, target, siteUrl, basePath } from './config.mjs';

const root = process.cwd();
const B = basePath;
const D = JSON.parse(fs.readFileSync(path.join(root, 'data/icerik.json'), 'utf8'));
const AMBLEM = fs.readFileSync(path.join(root, 'src/amblem.svg'), 'utf8').trim();
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const img = (ad) => `${B}images/${ad}.webp`;

// Netlify hedefinde form Netlify Forms'a düşer; Pages'te arayüz demo kalır.
const netlifyForm = target === 'netlify';

const marka = (koyu = false) => `<a class="marka" href="${B}" aria-label="${esc(D.marka.ad)} ana sayfa">
  ${AMBLEM}<span><b style="color:${koyu ? '#F5F3F0' : 'inherit'}">${D.marka.kisa}</b>
  <span>${D.marka.alt}</span></span></a>`;

function ustBar(aktif) {
  const bag = (slug, ad) =>
    `<a href="${B}${slug}/"${aktif === slug ? ' aria-current="page"' : ''}>${ad}</a>`;
  const menu = D.kollar.map((k) => bag(k.slug, k.ad.toUpperCase())).join('');
  return `<header class="ust">
  ${marka()}
  <nav class="menu" aria-label="Ana menü">${menu}<a href="${B}#iletisim">İLETİŞİM</a></nav>
  <div class="ust-sag">
    <a class="tel" href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a>
    <a class="btn" href="${B}#teklif">TEKLİF AL</a>
    <button class="hamburger" id="mnu" aria-label="Menüyü aç" aria-expanded="false" aria-controls="mobil">
      <span></span><span></span><span></span></button>
  </div>
</header>
<nav class="mobil-menu" id="mobil" aria-label="Mobil menü">
  ${D.kollar.map((k) => `<a href="${B}${k.slug}/">${k.ad.toUpperCase()}</a>`).join('')}
  <a href="${B}#iletisim">İLETİŞİM</a>
  <a href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a>
</nav>`;
}

const tik = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="2" aria-hidden="true"><path d="M4 12l6 6L20 6"/></svg>`;

function secici(secenekler, ters = false) {
  const dugme = secenekler.map((s, i) =>
    `<button role="tab" id="sk${i}" aria-controls="sp${i}" aria-selected="${i === 0}" data-hedef="sp${i}">${esc(s.kod)}</button>`).join('');
  const panel = secenekler.map((s, i) => `
    <div class="detay${ters ? ' ters' : ''}" id="sp${i}" role="tabpanel" aria-labelledby="sk${i}"${i ? ' hidden' : ''}>
      ${ters ? '' : `<div class="detay-gorsel"><img src="${img(s.gorsel)}" alt="${esc(s.ad)} uygulaması" loading="lazy"></div>`}
      <div class="detay-yazi">
        <div class="mono" style="font-size:12px;color:var(--bronz);letter-spacing:.1em">${esc(s.kod)}</div>
        <h2>${esc(s.ad)}</h2>
        <p>${esc(s.aciklama)}</p>
        <div class="ayrac"></div>
        <div style="font-size:11px;letter-spacing:.2em;color:var(--gri);margin-bottom:14px">KAPSAM</div>
        <ul class="kontrol">${s.liste.map((l) => `<li>${tik}<span>${esc(l)}</span></li>`).join('')}</ul>
        <div style="flex-grow:1"></div>
        <a class="btn" style="margin-top:28px" href="${B}#teklif">BU SEÇENEK İÇİN TEKLİF AL</a>
      </div>
      ${ters ? `<div class="detay-gorsel"><img src="${img(s.gorsel)}" alt="${esc(s.ad)} uygulaması" loading="lazy"></div>` : ''}
    </div>`).join('');
  return `<div class="secici" role="tablist" aria-label="Seçenekler">${dugme}</div>${panel}`;
}

function iletisim() {
  const alanlar = D.kollar.map((k) => `<option>${esc(k.ad)}</option>`).join('');
  const formAcik = netlifyForm
    ? `<form class="form" name="teklif" method="POST" action="${B}tesekkurler/" data-netlify="true" netlify-honeypot="bot-field">
       <input type="hidden" name="form-name" value="teklif">
       <p class="hp"><label>Bu alanı boş bırakın <input name="bot-field"></label></p>`
    : `<form class="form" onsubmit="event.preventDefault();alert('Form arayüzü hazır.')">`;
  return `<section class="iletisim" id="iletisim">
  <div>
    <div class="eyebrow">SİPARİŞ HATTI</div>
    <h2 id="teklif">Projenizi anlatın,<br>ölçüsünü birlikte alalım</h2>
    <p style="font-size:14.5px;line-height:1.8;color:var(--metin);margin-top:20px;max-width:420px">
      Tiny house, mobilya ya da karavan — ihtiyacınızı yazın, size uygun çözümü ve gerçekçi bir takvimi çıkaralım.</p>
    <div style="display:flex;flex-direction:column;gap:16px;margin-top:34px">
      <a class="satir" href="tel:${D.marka.telefonHam}">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="1.6" aria-hidden="true"><path d="M4 5c0-.6.4-1 1-1h3l2 5-2.5 1.5a12 12 0 0 0 5 5L14 13l5 2v3c0 .6-.4 1-1 1A15 15 0 0 1 4 5z"/></svg>
        <span class="mono" style="font-size:18px;color:var(--ink)">${D.marka.telefon}</span></a>
      <a class="satir" href="mailto:${D.marka.eposta}">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14"/><path d="M3 6l9 7 9-7"/></svg>
        <span style="color:var(--ink)">${D.marka.eposta}</span></a>
      <a class="satir" href="https://wa.me/${D.marka.telefonHam.replace('+', '')}" rel="noopener">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="1.6" aria-hidden="true"><path d="M12 3a9 9 0 0 0-7.7 13.6L3 21l4.5-1.2A9 9 0 1 0 12 3z"/></svg>
        <span style="color:var(--ink)">WhatsApp'tan yazın</span></a>
    </div>
  </div>
  ${formAcik}
    <div><label for="ad">AD SOYAD</label><input id="ad" name="ad" required autocomplete="name"></div>
    <div><label for="tel">TELEFON</label><input id="tel" name="telefon" type="tel" required autocomplete="tel"></div>
    <div><label for="alan">İLGİLENDİĞİNİZ ALAN</label><select id="alan" name="alan">${alanlar}</select></div>
    <div><label for="msj">MESAJ</label><textarea id="msj" name="mesaj"></textarea></div>
    <button class="btn" type="submit" style="margin-top:4px">TEKLİF TALEBİ GÖNDER</button>
  </form>
</section>`;
}

const altBilgi = () => `<footer class="alt">
  <div>
    <b>${D.marka.kisa}</b><small>${D.marka.alt}</small>
    <p>Tiny house · Modüler yapı · Mobilya · Karavan<br>
      <a href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a> · ${D.marka.eposta}</p>
  </div>
  <div class="telif">© ${new Date().getFullYear()} ${D.marka.ad.toUpperCase()}</div>
</footer>`;

const JS = `<script>
(function(){
  var m=document.getElementById('mnu'),n=document.getElementById('mobil');
  if(m&&n)m.addEventListener('click',function(){
    var a=n.classList.toggle('acik');m.setAttribute('aria-expanded',a);
    m.setAttribute('aria-label',a?'Menüyü kapat':'Menüyü aç');});
  document.querySelectorAll('[role=tablist]').forEach(function(t){
    var d=[].slice.call(t.querySelectorAll('[data-hedef]'));
    d.forEach(function(b){b.addEventListener('click',function(){
      d.forEach(function(o){
        o.setAttribute('aria-selected',o===b);
        var p=document.getElementById(o.dataset.hedef);
        if(p)p.hidden=(o!==b);});});});});
})();
</script>`;

function belge({ baslik, desc, slug, govde, aktif, sema }) {
  const canonical = `${siteUrl}/${slug ? slug + '/' : ''}`;
  return `<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(baslik)}</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="${esc(D.marka.ad)}">
<meta property="og:title" content="${esc(baslik)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${siteUrl}/images/img-16.webp">
<meta property="og:locale" content="tr_TR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2F3336">
<link rel="icon" href="${B}amblem.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Questrial&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="${B}styles.css">
<script type="application/ld+json">${JSON.stringify(sema)}</script>
</head>
<body>
${ustBar(aktif)}
<main>${govde}</main>
${altBilgi()}
${JS}
</body>
</html>`;
}

const kurulus = {
  '@context': 'https://schema.org', '@type': 'Organization',
  name: D.marka.ad, url: siteUrl + '/', logo: `${siteUrl}/amblem.svg`,
  telephone: D.marka.telefon, email: D.marka.eposta,
  address: { '@type': 'PostalAddress', addressCountry: 'TR' },
  description: 'Tiny house, ölçüye özel mobilya ve karavan üretimi. 7 yıllık deneyim, yaklaşık 200 tamamlanmış iş.'
};

// ───────────────────────────────────────────── ana sayfa
function anaSayfa() {
  const rakam = D.rakamlar.map((r) =>
    `<div><b${r.vurgu ? ' class="vurgu"' : ''}>${esc(r.sayi)}</b><span>${esc(r.etiket)}</span></div>`).join('');
  const kart = D.kollar.map((k) => `<article class="kart">
      <img src="${img(k.gorsel)}" alt="${esc(k.ad)} üretimi" loading="lazy" width="720" height="480">
      <div class="kart-ic">
        <div class="mono" style="font-size:11px;color:var(--bronz);letter-spacing:.1em">${k.no}</div>
        <h3>${esc(k.ad)}</h3><p>${esc(k.ozet)}</p>
        <ul class="etiketler">${k.etiketler.map((e) => `<li>${esc(e)}</li>`).join('')}</ul>
        <a class="devam" href="${B}${k.slug}/">İNCELE →</a>
      </div></article>`).join('');
  const surec = D.surec.map((s) =>
    `<div><div class="mono" style="font-size:12px;color:${s.no === '01' ? 'var(--bronz)' : 'var(--gri)'}">${s.no}</div>
     <h3>${esc(s.ad)}</h3><p>${esc(s.metin)}</p></div>`).join('');

  const govde = `<section class="hero">
  <img src="${img('img-16')}" alt="Global Yapı Geliştirme tiny house üretimi" width="1440" height="900" fetchpriority="high">
  <div class="hero-ic">
    <div class="rozet"><i></i><span class="eyebrow">KÖYÜM AKMEŞE · 260 ÜNİTELİK ÜRETİM SÜRÜYOR</span></div>
    <h1>Tiny house, mobilya ve karavanda tek üretim çatısı</h1>
    <p>Yedi yıllık üretim deneyimi ve yaklaşık 200 tamamlanmış iş. Proje bazlı seri üretim de,
       kişiye özel tek ünite de aynı atölyeden çıkar.</p>
    <div class="aksiyon"><a class="btn" href="#teklif">TEKLİF AL</a>
      <a class="btn ters" href="${B}tiny-house/">MODELLERİ İNCELE</a></div>
  </div></section>

<div class="rakamlar">${rakam}</div>

<section class="bolum">
  <div class="bolum-bas">
    <div><div class="eyebrow">NE ÜRETİYORUZ</div><h2>Üç kol, tek atölye</h2></div>
    <p>Şasiden mutfağa, konstrüksiyondan dolap kapağına kadar üretim kendi tesisimizde yapılır.</p>
  </div>
  <div class="kartlar">${kart}</div>
</section>

<section class="bant">
  <img src="${img('img-35')}" alt="Üretim tesisi" loading="lazy">
  <div class="bant-ic">
    <div class="rozet"><i></i><span class="eyebrow">DEVAM EDEN PROJE</span></div>
    <h2>${esc(D.akmese.baslik)}</h2><p>${esc(D.akmese.metin)}</p>
    <div class="bant-say">
      <div><b style="color:var(--bronz)">260</b><span>TOPLAM ÜNİTE</span></div>
      <div><b style="color:var(--kagit)">Aktif</b><span>ÜRETİM DURUMU</span></div>
    </div>
  </div></section>

<section class="bolum beyaz">
  <div class="eyebrow">NASIL ÇALIŞIYORUZ</div>
  <h2 style="font-size:clamp(26px,3.4vw,38px);margin:12px 0 40px">İhtiyaçtan anahtar teslime</h2>
  <div class="surec">${surec}</div>
</section>

${iletisim()}`;

  return belge({
    baslik: 'Tiny House, Mobilya ve Karavan Üretimi | Global Yapı Geliştirme',
    desc: 'Tiny house, ölçüye özel mobilya ve karavan üretimi. 7 yıllık deneyim, yaklaşık 200 tamamlanmış iş; Köyüm Akmeşe projesinde 260 ünitelik üretim sürüyor.',
    slug: '', govde, aktif: '',
    sema: { ...kurulus, '@type': ['Organization', 'LocalBusiness'] }
  });
}

// ───────────────────────────────────────────── kol sayfası
function kolSayfasi(k, i) {
  const ek = k.ek ? `<section class="bolum" style="padding-top:0">
    <div class="detay ters" style="background:var(--beyaz);border:1px solid var(--cizgi)">
      <div style="padding:44px 38px">
        <div class="eyebrow">İÇ MEKÂN</div>
        <h2 style="font-size:clamp(23px,2.6vw,32px);margin-top:14px">${esc(k.ek.baslik)}</h2>
        <p style="font-size:14px;line-height:1.85;color:var(--metin);margin-top:18px">${esc(k.ek.metin)}</p>
      </div>
      <img src="${img(k.ek.gorsel)}" alt="${esc(k.ek.baslik)}" loading="lazy" style="width:100%;height:100%;min-height:300px;object-fit:cover">
    </div></section>` : '';
  const not = k.not ? `<section class="bolum" style="padding-top:0">
    <div style="background:var(--beyaz);border:1px solid var(--cizgi);padding:38px 40px;display:flex;gap:24px;align-items:flex-start">
      <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="1.5" style="flex-shrink:0" aria-hidden="true"><path d="M12 3l8 4v5c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V7z"/><path d="M9 12l2 2 4-4"/></svg>
      <div><h3 style="font-size:21px">${esc(k.not.baslik)}</h3>
        <p style="font-size:14px;line-height:1.85;color:var(--metin);margin-top:10px">${esc(k.not.metin)}</p></div>
    </div></section>` : '';
  const akmese = k.slug === 'tiny-house' ? `<section class="bant">
    <img src="${img('img-35')}" alt="Üretim tesisi" loading="lazy">
    <div class="bant-ic"><div class="rozet"><i></i><span class="eyebrow">DEVAM EDEN PROJE</span></div>
      <h2>${esc(D.akmese.baslik)}</h2><p>${esc(D.akmese.metin)}</p></div></section>` : '';

  const govde = `<section class="sayfa-bas">
  <div class="eyebrow">ÜRETİM KOLU ${k.no}</div>
  <div class="satir" style="margin-top:14px"><h1>${esc(k.ad)}</h1><p>${esc(k.giris)}</p></div>
</section>
<section class="bolum">
  <div class="eyebrow" style="margin-bottom:18px">SEÇENEKLER</div>
  ${secici(k.secenekler, i === 1)}
</section>
${ek}${not}${akmese}${iletisim()}`;

  return belge({
    baslik: `${k.seo} | Global Yapı Geliştirme`,
    desc: k.desc, slug: k.slug, govde, aktif: k.slug,
    sema: {
      '@context': 'https://schema.org', '@type': 'Service',
      name: k.ad, description: k.desc, provider: kurulus,
      areaServed: { '@type': 'Country', name: 'Türkiye' },
      hasOfferCatalog: {
        '@type': 'OfferCatalog', name: `${k.ad} seçenekleri`,
        itemListElement: k.secenekler.map((s) => ({
          '@type': 'Offer', itemOffered: { '@type': 'Service', name: s.ad, description: s.aciklama }
        }))
      }
    }
  });
}

function yardimci(baslik, metin) {
  return belge({
    baslik: `${baslik} | ${D.marka.ad}`, desc: metin, slug: '', aktif: '',
    sema: kurulus,
    govde: `<section class="bolum" style="min-height:52vh;display:flex;flex-direction:column;justify-content:center">
      <div class="eyebrow">${esc(D.marka.kisa)}</div>
      <h1 style="font-size:clamp(30px,4vw,46px);margin:14px 0 18px">${esc(baslik)}</h1>
      <p style="font-size:15px;color:var(--metin);max-width:520px">${esc(metin)}</p>
      <a class="btn" style="margin-top:30px;align-self:flex-start" href="${B}">ANA SAYFAYA DÖN</a>
    </section>`
  });
}

// ───────────────────────────────────────────── yazım
const dist = path.join(root, 'dist');
fs.rmSync(dist, { recursive: true, force: true });
fs.mkdirSync(dist, { recursive: true });
fs.cpSync(path.join(root, 'public'), dist, { recursive: true });
fs.copyFileSync(path.join(root, 'src/styles.css'), path.join(dist, 'styles.css'));
fs.copyFileSync(path.join(root, 'src/amblem.svg'), path.join(dist, 'amblem.svg'));

fs.writeFileSync(path.join(dist, 'index.html'), anaSayfa());
D.kollar.forEach((k, i) => {
  const d = path.join(dist, k.slug);
  fs.mkdirSync(d, { recursive: true });
  fs.writeFileSync(path.join(d, 'index.html'), kolSayfasi(k, i));
});
fs.writeFileSync(path.join(dist, '404.html'),
  yardimci('Sayfa bulunamadı', 'Aradığınız sayfa taşınmış veya kaldırılmış olabilir.'));
if (netlifyForm) {
  const t = path.join(dist, 'tesekkurler');
  fs.mkdirSync(t, { recursive: true });
  fs.writeFileSync(path.join(t, 'index.html'),
    yardimci('Teklif talebiniz alındı', 'En kısa sürede sizinle iletişime geçeceğiz.'));
}

const yollar = ['', ...D.kollar.map((k) => k.slug)];
fs.writeFileSync(path.join(dist, 'sitemap.xml'),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
  yollar.map((s) => `  <url><loc>${siteUrl}/${s ? s + '/' : ''}</loc>` +
    `<changefreq>monthly</changefreq><priority>${s ? '0.8' : '1.0'}</priority></url>`).join('\n') +
  `\n</urlset>\n`);
fs.writeFileSync(path.join(dist, 'robots.txt'),
  `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}/sitemap.xml\n`);

console.log(`Built ${yollar.length} pages | target=${target} | base=${B} | url=${siteUrl}`);
