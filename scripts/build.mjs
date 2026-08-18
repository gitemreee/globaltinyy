import fs from 'node:fs';
import path from 'node:path';
import { site, target, siteUrl, basePath } from './config.mjs';

const root = process.cwd();
const B = basePath;
const D = JSON.parse(fs.readFileSync(path.join(root, 'data/icerik.json'), 'utf8'));
const AMBLEM = fs.readFileSync(path.join(root, 'src/amblem.svg'), 'utf8').trim();
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const img = (ad) => `${B}images/${ad}.webp`;
const netlifyForm = target === 'netlify';

/* ---------- simgeler (ince çizgi) ---------- */
const S = (d, o = 22, ek = '') => `<svg width="${o}" height="${o}" viewBox="0 0 24 24" fill="none" ` +
  `stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" ${ek} aria-hidden="true">${d}</svg>`;
const IK = {
  atolye: S('<path d="M3 21V9l5 3V9l5 3V9l5 3v9z"/><path d="M3 21h18"/><path d="M7 21v-4h3v4"/>'),
  anahtar: S('<path d="M14.5 6.5a4.5 4.5 0 1 0-4.2 6.2L4 19v2h3l1-1h2v-2h2v-2l2.2-2.2a4.5 4.5 0 0 0 .3-7.3z"/><circle cx="16.5" cy="7.5" r="1"/>'),
  kisi: S('<circle cx="12" cy="8" r="3.4"/><path d="M4.5 20a7.5 7.5 0 0 1 15 0"/>'),
  saat: S('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>', 20),
  onay: S('<circle cx="12" cy="12" r="8.5"/><path d="M8.5 12.2l2.4 2.4 4.6-4.8"/>', 20),
  ev: S('<path d="M4 10.5 12 4l8 6.5V20H4z"/><path d="M9.5 20v-5h5v5"/>', 20),
  katman: S('<path d="M12 3.5 3.5 8 12 12.5 20.5 8z"/><path d="M3.5 12 12 16.5 20.5 12"/><path d="M3.5 16 12 20.5 20.5 16"/>', 20),
  tel: S('<path d="M4.5 5.2c0-.7.6-1.2 1.2-1.2h2.6l1.6 4-2 1.3a12.5 12.5 0 0 0 5.3 5.3l1.3-2 4 1.6v2.6c0 .7-.5 1.2-1.2 1.2A16.5 16.5 0 0 1 4.5 5.2z"/>'),
  posta: S('<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3.6 7 12 13l8.4-6"/>'),
  wa: S('<path d="M12 3.2a8.8 8.8 0 0 0-7.5 13.4L3.2 20.8l4.4-1.2A8.8 8.8 0 1 0 12 3.2z"/><path d="M9 9.4c.2 2.2 2.4 4.4 4.6 4.6l1-1.2 1.7.8-.3 1.3c-2.9.5-6.4-3-5.9-5.9l1.3-.3.8 1.7z"/>'),
  kalem: S('<path d="M4 20h4L20 8a2.5 2.5 0 0 0-3.5-3.5L4.5 16.5z"/>', 20),
  kutu: S('<path d="M3.5 7.5 12 3.5l8.5 4v9L12 20.5 3.5 16.5z"/><path d="M3.5 7.5 12 11.7l8.5-4.2M12 11.7v8.8"/>', 20),
  kalkan: S('<path d="M12 3.2 19.5 6v5.4c0 4.3-3.1 8-7.5 9.4-4.4-1.4-7.5-5.1-7.5-9.4V6z"/><path d="M9 12l2 2 4-4"/>'),
  yildiz: S('<path d="M12 3.8 14.3 9l5.7.5-4.3 3.8 1.3 5.6L12 15.9 7 18.9l1.3-5.6L4 9.5 9.7 9z"/>', 18),
};
const TIK = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B87333" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 12.5l4.5 4.5 10-10"/></svg>`;
const OKS = (yon) => `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${yon === 'sol' ? 'M14.5 5 8 12l6.5 7' : 'M9.5 5 16 12l-6.5 7'}"/></svg>`;

/* ---------- parçalar ---------- */
const markaKilidi = () => `<a class="marka" href="${B}" aria-label="${esc(D.marka.ad)} — ana sayfa">
  ${AMBLEM}<span><b>${D.marka.kisa}</b><i>${D.marka.alt}</i></span></a>`;

function ustBar(aktif) {
  const bag = (slug, ad) => `<a href="${B}${slug}/"${aktif === slug ? ' aria-current="page"' : ''}>${ad}</a>`;
  return `<header class="ust">
  <div class="ust-ic">
    ${markaKilidi()}
    <nav class="nav" id="nav" aria-label="Ana menü">
      <a href="${B}"${aktif === '' ? ' aria-current="page"' : ''}>Ana Sayfa</a>
      ${D.kollar.map((k) => bag(k.slug, k.ad)).join('')}
      <a href="${B}#surec">Süreç</a>
      <a href="${B}#iletisim">İletişim</a>
    </nav>
    <div class="ust-sag">
      <a class="tel" href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a>
      <a class="dg koyu" href="${B}#teklif">Teklif Al</a>
      <button class="ham" id="mnu" aria-expanded="false" aria-controls="nav">Menü</button>
    </div>
  </div>
</header>`;
}

const gorselKart = (gorsel, alt, baslik, satir, { cip, sim, uzun, bag } = {}) => {
  const et = bag ? 'a' : 'div';
  return `<${et} class="gk${uzun ? ' uzun' : ''}"${bag ? ` href="${bag}"` : ''}>
    <img src="${img(gorsel)}" alt="${esc(alt)}" loading="lazy">
    ${sim ? `<span class="sim" style="color:#fff">${sim}</span>` : ''}
    ${cip ? `<span class="cip">${esc(cip)}</span>` : ''}
    <div class="alt"><h3>${esc(baslik)}</h3>
      <div class="satir">${satir}</div></div>
  </${et}>`;
};

const surecBandi = () => `<section class="bolum" id="surec">
  <div class="ic panel">
    <div class="bas">
      <div><span class="etiket">${IK.kalem}Nasıl çalışıyoruz</span>
        <h2 class="b2" style="margin-top:12px">Beş adımda anahtar teslim</h2></div>
      <p>İlk görüşmeden yerinde montaja kadar tek muhatap; her adımda ne olacağını önceden biliyorsunuz.</p>
    </div>
    <div class="adimlar">${D.surec.map((s) => `<div class="adim">
      <span class="no">${s.no}</span><h3>${esc(s.ad)}</h3><p>${esc(s.metin)}</p></div>`).join('')}</div>
  </div>
</section>`;

function iletisim() {
  const alanlar = D.kollar.map((k) => `<option>${esc(k.ad)}</option>`).join('');
  const ac = netlifyForm
    ? `<form name="teklif" method="POST" action="${B}tesekkurler/" data-netlify="true" netlify-honeypot="bot-field">
       <input type="hidden" name="form-name" value="teklif">
       <p class="gizli"><label>Bu alanı boş bırakın <input name="bot-field"></label></p>`
    : `<form onsubmit="event.preventDefault();alert('Form arayüzü hazır.')">`;
  return `<section class="bolum son" id="iletisim">
  <div class="ic panel">
    <div class="iletisim">
      <div>
        <span class="etiket">${IK.tel}Sipariş hattı</span>
        <h2 class="b1" style="margin:14px 0 12px">Projenizi anlatın,<br>ölçüsünü birlikte alalım</h2>
        <p class="lead">Tiny house, mobilya ya da karavan — ihtiyacınızı yazın; uygun çözümü ve
          gerçekçi bir teslim takvimini birlikte çıkaralım.</p>
        <div class="kanal">
          <a href="tel:${D.marka.telefonHam}"><span class="sim">${IK.tel}</span>
            <span><small>Telefon</small><b>${D.marka.telefon}</b></span></a>
          <a href="mailto:${D.marka.eposta}"><span class="sim">${IK.posta}</span>
            <span><small>E-posta</small><b>${D.marka.eposta}</b></span></a>
          <a href="https://wa.me/${D.marka.telefonHam.replace('+', '')}" rel="noopener"><span class="sim">${IK.wa}</span>
            <span><small>WhatsApp</small><b>Hemen mesaj gönderin</b></span></a>
        </div>
      </div>
      <div class="panel beyaz" id="teklif">
        <h3 class="b3">Teklif formu</h3>
        <p style="font-size:.875rem;margin-top:6px">Formu bırakın, aynı gün dönüş yapalım.</p>
        ${ac}
          <label>Ad soyad<input name="ad" required autocomplete="name" placeholder="Adınız ve soyadınız"></label>
          <label>Telefon<input name="telefon" type="tel" required autocomplete="tel" placeholder="05xx xxx xx xx"></label>
          <label>İlgilendiğiniz alan<select name="alan">${alanlar}</select></label>
          <label>Mesaj<textarea name="mesaj" placeholder="Ölçü, kullanım amacı, kurulum yeri…"></textarea></label>
          <button class="dg koyu" type="submit" style="width:100%;padding:15px">Teklif talebi gönder</button>
        </form>
      </div>
    </div>
  </div>
</section>`;
}

const altBilgi = () => `<footer class="alt">
  <div class="alt-ic">
    <div class="alt-ust">
      <div>
        <span style="display:inline-block">${AMBLEM.replace(/#2F3336/g, '#FFFFFF').replace('<svg', '<svg class="amb"')}</span>
        <p>${esc(D.marka.ad)} — tiny house, modüler yapı, ölçüye özel mobilya ve
           karavan üretimi. Tasarımdan montaja tek muhatap.</p>
      </div>
      <div><h4>Üretim kolları</h4>
        ${D.kollar.map((k) => `<a href="${B}${k.slug}/">${esc(k.ad)}</a>`).join('')}</div>
      <div><h4>İletişim</h4>
        <a href="tel:${D.marka.telefonHam}">${D.marka.telefon}</a>
        <a href="mailto:${D.marka.eposta}">${D.marka.eposta}</a>
        <a href="${B}#teklif">Teklif al</a></div>
    </div>
    <div class="alt-son">
      <span>© ${new Date().getFullYear()} ${esc(D.marka.ad)}</span>
      <span>globalyapicelik.net</span>
    </div>
  </div>
</footer>`;

const JS_ = `<script>
(function(){
  var m=document.getElementById('mnu'),n=document.getElementById('nav');
  function dar(){return window.matchMedia('(max-width:1080px)').matches}
  function kur(){if(n)n.hidden=dar()&&m.getAttribute('aria-expanded')!=='true'}
  if(m&&n){m.addEventListener('click',function(){
    m.setAttribute('aria-expanded',m.getAttribute('aria-expanded')!=='true');kur();});
   window.addEventListener('resize',kur);kur();}
  document.querySelectorAll('[data-ray]').forEach(function(g){
    var r=document.getElementById(g.dataset.ray);if(!r)return;
    g.querySelectorAll('button').forEach(function(b){
      b.addEventListener('click',function(){
        r.scrollBy({left:(b.dataset.yon==='sol'?-1:1)*(r.clientWidth*0.8),behavior:'smooth'});});});
  });
  document.querySelectorAll('[role=tablist]').forEach(function(t){
    var d=[].slice.call(t.querySelectorAll('[data-hedef]'));
    d.forEach(function(b){b.addEventListener('click',function(){
      d.forEach(function(o){o.setAttribute('aria-selected',o===b);
        var p=document.getElementById(o.dataset.hedef);if(p)p.hidden=(o!==b);});});});});
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Questrial&family=Inter:wght@400;500;600;700&display=swap">
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

// ───────────────────────────────────────────── ana sayfa
function anaSayfa() {
  const rkSim = [IK.saat, IK.onay, IK.ev, IK.katman];
  const rakamlar = D.rakamlar.map((r, i) => `<div class="rk">
    <span class="sim">${rkSim[i]}</span><b${r.vurgu ? ' style="color:var(--bronz)"' : ''}>${esc(r.sayi)}</b>
    <span>${esc(r.etiket.replace(' · ', '<br>'))}</span></div>`)
    .join('').replace(/&lt;br&gt;/g, '<br>');

  const ozellikler = [
    [IK.atolye, 'Kendi atölyemiz', 'Fason değil, kontrollü üretim. Çelik konstrüksiyon, ahşap işçiliği ve mobilya aynı çatı altında.'],
    [IK.anahtar, 'Anahtar teslim', 'Elektrik, tesisat, iç mekân ve mobilya dahil; çalışır halde teslim ediyoruz.'],
    [IK.kisi, 'Tek muhatap', 'Tasarımdan montaja kadar tek sorumluluk. Tedarikçiler arası gecikme yok.'],
  ].map(([s, b, m]) => `<div class="oz"><span class="sim">${s}</span>
      <div><h3>${b}</h3><p>${m}</p></div></div>`).join('');

  const kolKartlari = D.kollar.map((k) => gorselKart(
    k.gorsel, `${k.ad} üretimi`, k.ad,
    k.etiketler.slice(0, 3).map((e) => `<b>${esc(e)}</b>`).join('<span>·</span>'),
    { uzun: true, bag: `${B}${k.slug}/`, cip: `Kol ${k.no}` })).join('');

  const th = D.kollar[0];
  const tipler = th.secenekler.map((s) => gorselKart(
    s.gorsel, `${s.ad} tiny house`, s.ad,
    `<span>${esc(s.liste[0])}</span>`,
    { cip: s.kod, bag: `${B}tiny-house/` })).join('');

  const govde = `
<section class="bolum">
  <div class="ic hero">
    <img src="${img('img-16')}" alt="Ahşap cepheli tiny house, doğa içinde" fetchpriority="high" width="1536" height="1023">
    <span class="hero-rozet"><i></i>Köyüm Akmeşe’de 260 ünitelik üretim sürüyor</span>
    <div class="hero-yazi">
      <h1>GLOBAL<sup>YAPI</sup></h1>
      <p>Tiny house, ölçüye özel mobilya ve karavan üretimi. Fabrikada üretilen, sahada kurulan
         yapılar — şasiden mutfağa kadar her şey kendi atölyemizden çıkar.</p>
      <div class="dgler">
        <a class="dg bronz" href="#teklif">Teklif Al</a>
        <a class="dg cam" href="${B}tiny-house/">Modelleri Keşfet</a>
      </div>
    </div>
  </div>
</section>

<section class="bolum">
  <div class="ic neden">
    <div>
      <h2 class="b1">Yedi yıldır, yaklaşık 200 iş.<br>Hepsi kendi atölyemizden.</h2>
      <p style="margin-top:16px">Bir tiny house’un şasisi de, içindeki mutfağı da, cephesindeki ahşap da
        aynı ekipten çıkıyor. Bunun somut faydası kontrol: tasarımdan montaja kadar süreç tek elde
        olduğu için ölçü hatası ve “kimin işi” tartışması ortadan kalkıyor.</p>
      <div class="dgler" style="margin-top:22px">
        <a class="dg koyu" href="${B}tiny-house/">Üretimi inceleyin</a>
        <a class="dg acik" href="tel:${D.marka.telefonHam}">${IK.tel}${D.marka.telefon}</a>
      </div>
      <div class="rakamlar">${rakamlar}</div>
    </div>
    <div class="ozellik">${ozellikler}</div>
  </div>
</section>

<section class="bolum">
  <div class="ic panel">
    <div class="bas">
      <div><span class="etiket">${IK.kutu}Üretim kolları</span>
        <h2 class="b2" style="margin-top:12px">Üç kol, tek atölye</h2></div>
      <p>Modüler yapıdan ölçüye özel mobilyaya, ticari karavandan yaşam karavanına;
         üçü de aynı ölçü diliyle üretiliyor.</p>
    </div>
    <div class="kartlar uc">${kolKartlari}</div>
  </div>
</section>

<section class="bolum">
  <div class="ic panel beyaz">
    <div class="bas">
      <div><span class="etiket">${IK.ev}Tiny house tipleri</span>
        <h2 class="b2" style="margin-top:12px">1+0’dan mega boya</h2></div>
      <p>Konut, ofis ve ticari kullanım için sekiz tip. Hepsi ölçüye göre yeniden planlanabiliyor.</p>
    </div>
    <div class="ray" id="ray1">${tipler}</div>
    <div class="serit-ust">
      <a class="dg acik" href="${B}tiny-house/">Tüm tipleri gör</a>
      <div class="ok" data-ray="ray1">
        <button data-yon="sol" aria-label="Geri kaydır">${OKS('sol')}</button>
        <button data-yon="sag" aria-label="İleri kaydır">${OKS('sag')}</button>
      </div>
    </div>
  </div>
</section>

<section class="bolum">
  <div class="ic kartlar uc">
    <div class="dk koyu">
      <div>
        <span class="etiket" style="background:rgba(255,255,255,.12);color:#E4C79E">${IK.kalkan}Devam eden proje</span>
        <h2 class="b2" style="margin:14px 0 0;color:#fff">${esc(D.akmese.baslik)}</h2>
        <p>${esc(D.akmese.metin)}</p>
      </div>
      <a class="dg bronz" href="${B}tiny-house/">Tiny house üretimi</a>
    </div>
    ${gorselKart('img-35', 'Üretim tesisinde tamamlanma aşamasındaki ünite', 'Üretim tesisi',
      '<span>Tamamlanma aşamasındaki ünite</span>', { uzun: true, sim: IK.atolye })}
    ${gorselKart('img-31', 'Nakliyeye hazır tiny house', 'Nakliye ve montaj',
      '<span>Yerinde kurulum, çalışır halde teslim</span>', { uzun: true, sim: IK.kutu })}
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
function kolSayfasi(k) {
  const dugme = k.secenekler.map((s, i) =>
    `<button role="tab" id="sk${i}" aria-controls="sp${i}" aria-selected="${i === 0}" data-hedef="sp${i}">${esc(s.ad)}</button>`).join('');
  const panel = k.secenekler.map((s, i) => `
    <div class="detay" id="sp${i}" role="tabpanel" aria-labelledby="sk${i}"${i ? ' hidden' : ''}>
      <div class="gorsel"><img src="${img(s.gorsel)}" alt="${esc(s.ad)} uygulaması" loading="lazy"></div>
      <div>
        <span class="etiket">${esc(s.kod)}</span>
        <h2 class="b2" style="margin:12px 0 10px">${esc(s.ad)}</h2>
        <p>${esc(s.aciklama)}</p>
        <ul class="liste">${s.liste.map((l) => `<li>${TIK}<span>${esc(l)}</span></li>`).join('')}</ul>
        <div class="dgler" style="margin-top:24px">
          <a class="dg koyu" href="${B}#teklif">Bu seçenek için teklif al</a>
          <a class="dg acik" href="tel:${D.marka.telefonHam}">${IK.tel}Ara</a>
        </div>
      </div>
    </div>`).join('');

  const ek = k.ek ? `<section class="bolum">
    <div class="ic panel beyaz detay">
      <div>
        <span class="etiket">${IK.atolye}Detay</span>
        <h2 class="b2" style="margin:12px 0 10px">${esc(k.ek.baslik)}</h2>
        <p class="lead">${esc(k.ek.metin)}</p>
      </div>
      <div class="gorsel"><img src="${img(k.ek.gorsel)}" alt="${esc(k.ek.baslik)}" loading="lazy"></div>
    </div></section>` : '';

  const not = k.not ? `<section class="bolum">
    <div class="ic panel beyaz" style="display:flex;gap:20px;align-items:flex-start">
      <span class="sim" style="flex:0 0 auto;width:48px;height:48px;border-radius:15px;background:var(--zemin);display:grid;place-items:center;color:var(--bronz)">${IK.kalkan}</span>
      <div><h3 class="b3">${esc(k.not.baslik)}</h3>
        <p style="margin-top:8px">${esc(k.not.metin)}</p></div>
    </div></section>` : '';

  const akmese = k.slug === 'tiny-house' ? `<section class="bolum">
    <div class="ic kartlar uc">
      <div class="dk koyu">
        <div><span class="etiket" style="background:rgba(255,255,255,.12);color:#E4C79E">${IK.kalkan}Devam eden proje</span>
          <h2 class="b2" style="margin:14px 0 0;color:#fff">${esc(D.akmese.baslik)}</h2>
          <p>${esc(D.akmese.metin)}</p></div>
        <a class="dg bronz" href="${B}#teklif">Bilgi alın</a>
      </div>
      ${gorselKart('img-35', 'Üretim tesisi', 'Üretim tesisi', '<span>Tamamlanma aşamasındaki ünite</span>', { uzun: true, sim: IK.atolye })}
      ${gorselKart('img-28', 'Merdiven içi depolama detayı', 'İç mekân detayı', '<span>Merdiven içi depolama</span>', { uzun: true, sim: IK.ev })}
    </div></section>` : '';

  const govde = `
<section class="bolum">
  <div class="ic hero" style="min-height:clamp(320px,36vw,420px)">
    <img src="${img(k.gorsel)}" alt="${esc(k.ad)} üretimi" fetchpriority="high">
    <span class="hero-rozet"><i></i>Üretim kolu ${k.no}</span>
    <div class="hero-yazi">
      <h1 style="font-size:clamp(2.25rem,1.2rem + 4vw,4rem);letter-spacing:-.02em;font-family:Inter,sans-serif;font-weight:700;line-height:1.05">${esc(k.ad)}</h1>
      <p style="margin-top:12px">${esc(k.giris)}</p>
      <div class="dgler"><a class="dg bronz" href="${B}#teklif">Teklif Al</a>
        <a class="dg cam" href="tel:${D.marka.telefonHam}">${IK.tel}${D.marka.telefon}</a></div>
    </div>
  </div>
</section>

<section class="bolum">
  <div class="ic panel">
    <div class="bas">
      <div><span class="etiket">${IK.katman}Seçenekler</span>
        <h2 class="b2" style="margin-top:12px">${esc(k.ad)} çeşitleri</h2></div>
      <p>Bir seçeneği açın; kapsamı, kullanım alanlarını ve uygulamadan bir kareyi görün.</p>
    </div>
    <div class="sekmeler" role="tablist" aria-label="${esc(k.ad)} seçenekleri">${dugme}</div>
    ${panel}
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
    baslik: `${baslik} | ${D.marka.ad}`, desc: metin, slug: '', aktif: '', sema: kurulus,
    govde: `<section class="bolum son">
      <div class="ic panel" style="min-height:46vh;display:flex;flex-direction:column;justify-content:center">
        <span class="etiket">${esc(D.marka.kisa)}</span>
        <h1 class="b1" style="margin:14px 0 12px">${esc(baslik)}</h1>
        <p class="lead">${esc(metin)}</p>
        <div class="dgler" style="margin-top:24px"><a class="dg koyu" href="${B}">Ana sayfaya dön</a></div>
      </div></section>`
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
D.kollar.forEach((k) => {
  const d = path.join(dist, k.slug);
  fs.mkdirSync(d, { recursive: true });
  fs.writeFileSync(path.join(d, 'index.html'), kolSayfasi(k));
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
