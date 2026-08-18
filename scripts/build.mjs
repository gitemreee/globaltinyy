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

/* Hayalet başlık: ilk satır tonlu, ikinci satır solid. */
const dt = (g, s, sinif = '') =>
  `<h2 class="dt${sinif ? ' ' + sinif : ''}"><span class="g">${esc(g)}</span><span class="s">${esc(s)}</span></h2>`;
const dt1 = (g, s, sinif = '') => dt(g, s, sinif).replace('<h2', '<h1').replace('</h2>', '</h1>');

/* Fotoğraf + alt yazı. Fotoğraflar küçük ve künyeli tutulur. */
const fig = (ad, alt, kap, sinif = 'f-yat', oncelik = false) =>
  `<figure><img src="${img(ad)}" alt="${esc(alt)}" class="${sinif}"${oncelik ? ' fetchpriority="high"' : ' loading="lazy"'}>` +
  (kap ? `<figcaption class="tiny">${esc(kap)}</figcaption>` : '') + `</figure>`;

const markaKilidi = () => `<a class="marka" href="${B}" aria-label="${esc(D.marka.ad)} — ana sayfa">
  ${AMBLEM}<span><b>${D.marka.kisa}</b><span>${D.marka.alt}</span></span></a>`;

function ustBar(aktif) {
  const bag = (slug, ad) =>
    `<a href="${B}${slug}/"${aktif === slug ? ' aria-current="page"' : ''}>${ad}</a>`;
  return `<header class="ust">
  <div class="ust-ic">
    ${markaKilidi()}
    <button class="hamburger" id="mnu" aria-expanded="false" aria-controls="nav">MENÜ</button>
    <nav class="nav" id="nav" aria-label="Ana menü">
      ${D.kollar.map((k) => bag(k.slug, k.ad)).join('')}
      <a href="${B}#iletisim">İletişim</a>
      <a class="tel" href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a>
    </nav>
  </div>
</header>`;
}

const tik = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="2.4" aria-hidden="true"><path d="M4 12l6 6L20 6"/></svg>`;

function secici(secenekler, ters = false) {
  const dugme = secenekler.map((s, i) =>
    `<button role="tab" id="sk${i}" aria-controls="sp${i}" aria-selected="${i === 0}" data-hedef="sp${i}">${esc(s.kod)}</button>`).join('');
  const panel = secenekler.map((s, i) => `
    <div class="detay${ters ? ' ters' : ''}" id="sp${i}" role="tabpanel" aria-labelledby="sk${i}"${i ? ' hidden' : ''}>
      ${fig(s.gorsel, `${s.ad} uygulaması`, s.ad.toUpperCase(), 'f-yat')}
      <div class="metin">
        <span class="kicker">SEÇENEK · ${esc(s.kod)}</span>
        <h2 class="dt xs"><span class="s">${esc(s.ad)}</span></h2>
        <p style="margin-top:14px">${esc(s.aciklama)}</p>
        <h4 style="margin-top:28px;color:var(--muted)">Kullanım</h4>
        <ul class="liste">${s.liste.map((l) => `<li>${tik}<span>${esc(l)}</span></li>`).join('')}</ul>
        <div class="dgler"><a class="dg" href="${B}#teklif">Bu seçenek için teklif al</a></div>
      </div>
    </div>`).join('');
  return `<div class="sekmeler" role="tablist" aria-label="Seçenekler">${dugme}</div>${panel}`;
}

function iletisim() {
  const alanlar = D.kollar.map((k) => `<option>${esc(k.ad)}</option>`).join('');
  const ac = netlifyForm
    ? `<form name="teklif" method="POST" action="${B}tesekkurler/" data-netlify="true" netlify-honeypot="bot-field">
       <input type="hidden" name="form-name" value="teklif">
       <p class="gizli"><label>Bu alanı boş bırakın <input name="bot-field"></label></p>`
    : `<form onsubmit="event.preventDefault();alert('Form arayüzü hazır.')">`;
  return `<section class="band pale" id="iletisim">
  <div class="ic iletisim">
    <div>
      <span class="kicker">Sipariş hattı</span>
      ${dt('Projenizi anlatın,', 'ölçüsünü birlikte alalım', 'sm')}
      <p class="lead" style="margin-top:20px">Tiny house, mobilya ya da karavan — ihtiyacınızı yazın;
         uygun çözümü ve gerçekçi bir takvimi birlikte çıkaralım.</p>
      <div class="bilgi" style="margin-top:34px">
        <a href="tel:${D.marka.telefonHam}"><span class="tiny">Telefon</span><b>${D.marka.telefon}</b></a>
        <a href="mailto:${D.marka.eposta}"><span class="tiny">E-posta</span><b>${D.marka.eposta}</b></a>
        <a href="https://wa.me/${D.marka.telefonHam.replace('+', '')}" rel="noopener"><span class="tiny">WhatsApp</span><b>Mesaj gönderin</b></a>
      </div>
    </div>
    <div id="teklif">
      <span class="kicker">Teklif formu</span>
      ${ac}
        <label><span class="tiny">Ad soyad</span><input name="ad" required autocomplete="name"></label>
        <label><span class="tiny">Telefon</span><input name="telefon" type="tel" required autocomplete="tel"></label>
        <label><span class="tiny">İlgilendiğiniz alan</span><select name="alan">${alanlar}</select></label>
        <label><span class="tiny">Mesaj</span><textarea name="mesaj" placeholder="Ölçü, kullanım amacı, kurulum yeri…"></textarea></label>
        <button class="dg dolu" type="submit" style="justify-content:center">Teklif talebi gönder</button>
      </form>
    </div>
  </div>
</section>`;
}

const altBilgi = () => `<footer class="alt">
  <div class="alt-ic">
    <div>
      ${AMBLEM.replace(/#2F3336/g, '#FFFFFF')}
      <p style="margin-top:18px;max-width:34ch">${esc(D.marka.ad)} — tiny house, modüler yapı,
         ölçüye özel mobilya ve karavan üretimi. Tasarımdan montaja tek muhatap.</p>
    </div>
    <div>
      <span class="kicker">Üretim kolları</span>
      ${D.kollar.map((k) => `<a href="${B}${k.slug}/">${esc(k.ad)}</a>`).join('')}
    </div>
    <div>
      <span class="kicker">İletişim</span>
      <a href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a>
      <a href="mailto:${D.marka.eposta}">${D.marka.eposta}</a>
      <a href="${B}#teklif">Teklif al</a>
    </div>
  </div>
  <div class="alt-son tiny">
    <span>© ${new Date().getFullYear()} ${esc(D.marka.ad)}</span>
    <span>globalyapicelik.net</span>
  </div>
</footer>`;

const JS_ = `<script>
(function(){
  var m=document.getElementById('mnu'),n=document.getElementById('nav');
  function dar(){return window.matchMedia('(max-width:1080px)').matches}
  function kur(){ if(n) n.hidden = dar() && m.getAttribute('aria-expanded')!=='true'; }
  if(m&&n){m.addEventListener('click',function(){
    var a=m.getAttribute('aria-expanded')!=='true';
    m.setAttribute('aria-expanded',a);m.textContent=a?'KAPAT':'MENÜ';kur();});
   window.addEventListener('resize',kur);kur();}
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Questrial&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="${B}styles.css">
<script type="application/ld+json">${JSON.stringify(sema)}</script>
</head>
<body>
${ustBar(aktif)}
<main>${govde}</main>
${altBilgi()}
${JS_}
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

const surecBandi = (baslik = 'anahtar teslime') => `<section class="band tan">
  <div class="ic">
    <span class="kicker">Nasıl çalışıyoruz</span>
    ${dt('İhtiyaçtan', baslik)}
    <div class="surec">${D.surec.map((s) =>
      `<div class="adim"><span class="no">${s.no}</span><h3>${esc(s.ad)}</h3><p>${esc(s.metin)}</p></div>`).join('')}</div>
  </div>
</section>`;

const rakamlar = () => `<div class="rakamlar">${D.rakamlar.map((r) =>
  `<div class="rakam${r.vurgu ? ' vurgu' : ''}"><b>${esc(r.sayi)}</b><span>${esc(r.etiket)}</span></div>`).join('')}</div>`;

// ───────────────────────────────────────────── ana sayfa
function anaSayfa() {
  const kol = D.kollar.map((k) => `<article class="kol">
    <div class="no">${k.no}</div>
    <div>
      <h2 class="dt sm"><span class="s">${esc(k.ad)}</span></h2>
      <p style="margin-top:16px">${esc(k.ozet)}</p>
      <div class="etiketler">${k.etiketler.map((e) => `<span>${esc(e)}</span>`).join('')}</div>
      <a class="bag" href="${B}${k.slug}/">${esc(k.ad)} sayfası</a>
    </div>
    ${fig(k.gorsel, `${k.ad} üretimi`, k.etiketler.slice(0, 2).join(' · '), 'f-yat')}
  </article>`).join('');


  const govde = `
<section class="kapak">
  <div class="kapak-bas">
    <div class="ust-cizgi"><hr class="hr"><span class="kicker" style="letter-spacing:.34em">GLOBAL</span><hr class="hr"></div>
    <div class="kapak-grid">
      <div>
        <span class="kicker">Yapı Geliştirme A.Ş. · 2019’dan beri</span>
        ${dt1('Tiny house, mobilya', 've karavan üretimi')}
        <hr class="hr-ink">
      </div>
      <div>
        <p class="lead">Fabrikada üretilen, sahada kurulan yapılar. Şasiden mutfağa,
          konstrüksiyondan dolap kapağına kadar her şey kendi atölyemizde çıkar —
          proje bazlı seri üretim de, kişiye özel tek ünite de.</p>
        <div class="dgler">
          <a class="dg dolu" href="#teklif">Teklif al</a>
          <a class="dg" href="${B}tiny-house/">Modelleri incele</a>
        </div>
      </div>
    </div>
  </div>
  <div class="serit">
    ${fig('img-16', 'Ahşap cepheli tiny house', 'TEKERLEKLİ MODEL · AHŞAP CEPHE', 'f-por', true)}
    ${fig('img-14', 'Tiny house iç mekân', 'İÇ MEKÂN · LOFT VE MUTFAK', 'f-por')}
    ${fig('img-01', 'A-frame gece görünümü', 'A-FRAME KÜTLE · GECE', 'f-por')}
  </div>
</section>

<section class="band tight">
  <div class="ic">${rakamlar()}</div>
</section>

<section class="band pale">
  <div class="ic">
    <div class="kapak-grid" style="align-items:start">
      <div>
        <span class="kicker">Ne üretiyoruz</span>
        ${dt('Üç üretim kolu,', 'tek atölye')}
      </div>
      <p class="lead">Üç iş de aynı ekiple, aynı ölçü diliyle yürür. Bir tiny house’un şasisi de,
        içindeki mutfağı da, cephesindeki ahşabı da aynı çatı altında üretilir.</p>
    </div>
    <div style="margin-top:clamp(34px,4vw,58px)">${kol}</div>
  </div>
</section>

<section class="band dark">
  <div class="ic">
    <div class="kapak-grid" style="align-items:start">
      <div>
        <span class="kicker">Devam eden proje</span>
        ${dt('Köyüm Akmeşe’de', '260 tiny house')}
      </div>
      <div>
        <p class="lead" style="color:#E6E2DA">${esc(D.akmese.metin)}</p>
        <div class="dgler"><a class="dg" href="${B}tiny-house/">Tiny house üretimi</a></div>
      </div>
    </div>
    <div class="serit" style="margin-top:clamp(38px,4.5vw,64px)">
      ${fig('img-35', 'Üretim tesisinde tamamlanma aşamasındaki ünite', 'ÜRETİM TESİSİ · TAMAMLANMA AŞAMASI', 'f-gen')}
      ${fig('img-31', 'Nakliyeye hazır tiny house', 'NAKLİYEYE HAZIR ÜNİTE', 'f-gen')}
      ${fig('img-28', 'Merdiven içi depolama detayı', 'MERDİVEN İÇİ DEPOLAMA', 'f-gen')}
    </div>
  </div>
</section>

${surecBandi()}

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
  const ek = k.ek ? `<section class="band pale">
    <div class="ic detay">
      ${fig(k.ek.gorsel, k.ek.baslik, 'İÇ MEKÂN UYGULAMASI', 'f-yat')}
      <div class="metin">
        <span class="kicker">Detay</span>
        ${dt('İçerideki her şey', 'bizim üretimimiz', 'sm')}
        <p style="margin-top:16px">${esc(k.ek.metin)}</p>
      </div>
    </div></section>` : '';

  const not = k.not ? `<section class="band tight">
    <div class="ic kutu">
      <span class="kicker">Mevzuat</span>
      <h3 style="margin:10px 0 12px;font-size:1.25rem">${esc(k.not.baslik)}</h3>
      <p>${esc(k.not.metin)}</p>
    </div></section>` : '';

  const akmese = k.slug === 'tiny-house' ? `<section class="band dark">
    <div class="ic kapak-grid" style="align-items:start">
      <div><span class="kicker">Devam eden proje</span>${dt('Köyüm Akmeşe’de', '260 tiny house')}</div>
      <p class="lead" style="color:#E6E2DA">${esc(D.akmese.metin)}</p>
    </div></section>` : '';

  const govde = `
<section class="band tan">
  <div class="ic sayfa-bas">
    <div>
      <span class="kicker">Üretim kolu ${k.no}</span>
      <h1 class="dt"><span class="g">Global</span><span class="s">${esc(k.ad)}</span></h1>
      <hr class="hr-ink">
    </div>
    <div>
      <p class="lead">${esc(k.giris)}</p>
      <div class="dgler"><a class="dg" href="#teklif">Teklif al</a></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="ic">
    <span class="kicker" style="display:block;margin-bottom:20px">Seçenekler</span>
    ${secici(k.secenekler, i === 1)}
  </div>
</section>
${ek}${not}${akmese}${surecBandi()}${iletisim()}`;

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
    govde: `<section class="band pale" style="min-height:56vh;display:flex;align-items:center">
      <div class="ic">
        <span class="kicker">${esc(D.marka.kisa)}</span>
        <h1 class="dt sm"><span class="s">${esc(baslik)}</span></h1>
        <p class="lead" style="margin-top:18px">${esc(metin)}</p>
        <div class="dgler"><a class="dg" href="${B}">Ana sayfaya dön</a></div>
      </div>
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
