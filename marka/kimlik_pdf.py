#!/usr/bin/env python3
"""
GLOBAL YAPI GELİŞTİRME A.Ş. — Marka Kimliği Rehberi üreteci.

Müşterinin mevcut kimlik dosyasının yapısı korundu; farkı mockup'larda:
düz vektör ikonlar yerine gölge, doku, perspektif ve malzeme hissi olan
sahneler kuruldu.

Amblem `amblem.py`'den gelir — çatı `TEPE` ile kısaltılmış durumda.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from amblem import amblem_svg, INK, BRONZ, GRI, KAGIT

TEPE = 70.0          # çatı kısaltması
BASE = os.path.dirname(os.path.abspath(__file__))


def amb(h, ink=INK, bronz=BRONZ, extra=''):
    return amblem_svg(TEPE, ink=ink, bronz=bronz).replace(
        '<svg', f'<svg style="height:{h};width:auto;{extra}"', 1)


def kilit(amb_h, tsize, ink=INK, bronz=BRONZ, alt=True, orta=True):
    """Dikey kilit: amblem → GLOBAL → açıklama."""
    hiza = 'center' if orta else 'left'
    isaret = amb(f'{amb_h}px', ink=ink, bronz=bronz)
    altsatir = (f'<div style="font-family:Inter;font-size:{tsize*0.235:.1f}px;'
                f'letter-spacing:.34em;color:{bronz};margin-top:{tsize*0.32:.1f}px;'
                f'text-indent:.34em">YAPI GELİŞTİRME A.Ş.</div>') if alt else ''
    return (f'<div style="text-align:{hiza}">'
            f'<div style="margin-bottom:{tsize*0.44:.1f}px">{isaret}</div>'
            f'<div style="font-family:Questrial;font-size:{tsize}px;letter-spacing:.30em;'
            f'color:{ink};line-height:1;text-indent:.30em">GLOBAL</div>{altsatir}</div>')


def yatay(amb_h, tsize, ink=INK, bronz=BRONZ):
    """Yatay kilit: amblem solda, yazı sağda."""
    isaret = amb(f'{amb_h:.0f}px', ink=ink, bronz=bronz)
    return (f'<div style="display:flex;align-items:center;gap:{amb_h*0.30:.0f}px">{isaret}'
            f'<div><div style="font-family:Questrial;font-size:{tsize:.1f}px;'
            f'letter-spacing:.28em;color:{ink};line-height:1">GLOBAL</div>'
            f'<div style="font-family:Inter;font-size:{tsize*0.225:.1f}px;letter-spacing:.32em;'
            f'color:{bronz};margin-top:{tsize*0.26:.1f}px">YAPI GELİŞTİRME A.Ş.</div>'
            f'</div></div>')


def sayfa(no, bolum, baslik, aciklama, icerik, koyu=False):
    zemin = INK if koyu else KAGIT
    yazi = KAGIT if koyu else INK
    return f'''<section class="page" style="background:{zemin};color:{yazi}">
      <div class="pad">
        <div class="ust">
          <span>GLOBAL YAPI GELİŞTİRME A.Ş. — MARKA KİMLİĞİ</span>
          <span style="color:{BRONZ}">{no} / {bolum}</span>
        </div>
        <h2>{baslik}</h2>
        <p class="alt">{aciklama}</p>
        {icerik}
        <div class="dip"><span>BAKIR BRONZ · QUESTRIAL · V2.0</span><span>GLOBALYAPI</span></div>
      </div></section>'''


# ═══════════════════════════════════════════════════ MOCKUP'LAR
# Hepsi CSS/SVG. Gerçekçilik gölge katmanları, yüzey gradyanları ve
# kağıt/kumaş dokusundan geliyor — düz vektör ikon değil.

DOKU = '''<svg width="0" height="0" style="position:absolute">
 <filter id="kagit"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4"/>
  <feColorMatrix values="0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0.06 0"/></filter>
 <filter id="kumas"><feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="3"/>
  <feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.10 0"/></filter>
</svg>'''

SAHNE = ('background:linear-gradient(150deg,#E6E2DB 0%,#D9D4CB 55%,#CFC9BF 100%);'
         'border-radius:2px;position:relative;overflow:hidden')
KAGIT_GOLGE = ('box-shadow:0 1px 2px rgba(40,36,32,.16),0 8px 18px rgba(40,36,32,.16),'
               '0 22px 44px rgba(40,36,32,.14)')


def _doku(op=1):
    return (f'<div style="position:absolute;inset:0;filter:url(#kagit);opacity:{op};'
            f'pointer-events:none;mix-blend-mode:multiply"></div>')


def zarf(w=300):
    """DL zarf — kapak katmanı, kenar gölgesi, kağıt dokusu."""
    h = w * 0.485
    return f'''<div style="width:{w}px;height:{h:.0f}px;position:relative;
      background:linear-gradient(168deg,#FCFBF8,#F1EEE8 70%,#E9E5DD);{KAGIT_GOLGE};border-radius:1px">
      {_doku()}
      <!-- kapak -->
      <div style="position:absolute;top:0;left:0;right:0;height:{h*0.56:.0f}px;
        background:linear-gradient(180deg,#F7F4EE,#EFEBE3);
        clip-path:polygon(0 0,100% 0,50% 100%);
        box-shadow:0 1px 0 rgba(0,0,0,.05)"></div>
      <div style="position:absolute;top:0;left:0;right:0;height:{h*0.56:.0f}px;
        border-bottom:0;background:transparent;
        background-image:linear-gradient(to bottom right,transparent 49.6%,rgba(0,0,0,.09) 50%,transparent 50.4%),
          linear-gradient(to bottom left,transparent 49.6%,rgba(0,0,0,.09) 50%,transparent 50.4%)"></div>
      <div style="position:absolute;left:{w*0.075:.0f}px;top:{h*0.115:.0f}px">
        {yatay(w*0.105, w*0.062)}</div>
      <div style="position:absolute;right:{w*0.07:.0f}px;bottom:{h*0.13:.0f}px;text-align:right;
        font-family:Inter;font-size:{w*0.030:.1f}px;line-height:1.85;color:#6A665F">
        Alıcı Ad Soyad<br>Mahalle, Cadde No: 00<br>34000 İstanbul / Türkiye</div>
      <div style="position:absolute;right:{w*0.055:.0f}px;top:{h*0.10:.0f}px;
        width:{w*0.115:.0f}px;height:{w*0.135:.0f}px;border:1px dashed #C9C3B8"></div>
    </div>'''


def antetli(w=210):
    """A4 antetli — hafif perspektif, sayfa kıvrım gölgesi."""
    h = w * 1.414
    return f'''<div style="width:{w}px;height:{h:.0f}px;position:relative;
      background:linear-gradient(105deg,#FDFCFA,#F4F1EB 60%,#EDE9E1);{KAGIT_GOLGE};
      transform:perspective(1400px) rotateY(-7deg) rotateX(1.5deg);transform-origin:left center">
      {_doku()}
      <div style="position:absolute;left:{w*0.10:.0f}px;top:{w*0.085:.0f}px">
        {yatay(w*0.115, w*0.068)}</div>
      <div style="position:absolute;left:{w*0.10:.0f}px;right:{w*0.10:.0f}px;top:{w*0.245:.0f}px;
        height:1px;background:{BRONZ};opacity:.55"></div>
      <div style="position:absolute;left:{w*0.10:.0f}px;right:{w*0.10:.0f}px;top:{w*0.315:.0f}px;
        font-family:Inter;font-size:{w*0.030:.1f}px;line-height:2.35;color:#8C8880">
        {'<div style="height:1px;background:#DCD7CE;margin:%.1fpx 0"></div>' % (w*0.028) * 13}</div>
      <div style="position:absolute;left:{w*0.10:.0f}px;right:{w*0.10:.0f}px;bottom:{w*0.075:.0f}px;
        font-family:Inter;font-size:{w*0.026:.1f}px;letter-spacing:.16em;color:#A9A49B;
        border-top:1px solid #DCD7CE;padding-top:{w*0.032:.0f}px">GLOBALYAPI.COM.TR</div>
    </div>'''


def kartvizit(w=250):
    """85×54 mm — iki kart, alttaki koyu, üstteki hafif döndürülmüş."""
    h = w * 0.635
    return f'''<div style="position:relative;width:{w*1.28:.0f}px;height:{h*1.5:.0f}px">
      <!-- alt kart (koyu yüz) -->
      <div style="position:absolute;left:0;top:{h*0.42:.0f}px;width:{w}px;height:{h:.0f}px;
        background:linear-gradient(145deg,#3A3F42,#2C3033 55%,#25292B);border-radius:2px;
        box-shadow:0 2px 4px rgba(20,18,16,.3),0 14px 30px rgba(20,18,16,.28);
        transform:rotate(-6deg);display:flex;align-items:center;justify-content:center">
        {kilit(w*0.155, w*0.088, ink=KAGIT, bronz=BRONZ)}
      </div>
      <!-- üst kart (açık yüz) -->
      <div style="position:absolute;left:{w*0.30:.0f}px;top:0;width:{w}px;height:{h:.0f}px;
        background:linear-gradient(150deg,#FDFCFA,#F3F0EA 70%,#EBE7DF);border-radius:2px;
        box-shadow:0 2px 4px rgba(40,36,32,.2),0 16px 34px rgba(40,36,32,.24);
        transform:rotate(3.5deg);overflow:hidden">
        {_doku()}
        <div style="position:absolute;left:{w*0.075:.0f}px;top:{h*0.145:.0f}px">
          {yatay(w*0.115, w*0.070)}</div>
        <div style="position:absolute;left:{w*0.075:.0f}px;bottom:{h*0.145:.0f}px;
          font-family:Inter;font-size:{w*0.036:.1f}px;line-height:1.95;color:#6A665F">
          <b style="color:{INK};font-size:{w*0.042:.1f}px">AD SOYAD</b><br>
          <span style="color:{BRONZ};letter-spacing:.08em">Yönetim Kurulu Başkanı</span><br>
          +90 000 000 00 00<br>ad@globalyapi.com.tr</div>
        <div style="position:absolute;right:{-w*0.02:.0f}px;bottom:{-h*0.10:.0f}px;opacity:.055">
          {amb(f'{h*0.85:.0f}px')}</div>
      </div></div>'''


def tisort(w=230):
    """Tişört — SVG siluet, kumaş gölgeleri ve kırışıklık."""
    return f'''<div style="position:relative;width:{w}px">
      <svg viewBox="0 0 300 340" style="width:100%;height:auto;display:block;
        filter:drop-shadow(0 14px 26px rgba(30,28,25,.30))">
        <defs><linearGradient id="tg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#3C4144"/><stop offset=".45" stop-color="#2E3335"/>
          <stop offset="1" stop-color="#23272A"/></linearGradient>
          <radialGradient id="tl" cx=".38" cy=".28" r=".6">
          <stop offset="0" stop-color="#fff" stop-opacity=".13"/>
          <stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>
        <path d="M104 22 L150 40 L196 22 L262 58 L238 108 L214 96 L214 322
                 Q150 332 86 322 L86 96 L62 108 L38 58 Z" fill="url(#tg)"/>
        <path d="M104 22 L150 40 L196 22 L262 58 L238 108 L214 96 L214 322
                 Q150 332 86 322 L86 96 L62 108 L38 58 Z" fill="url(#tl)"/>
        <path d="M104 22 Q150 62 196 22 Q150 50 104 22 Z" fill="#1B1F21" opacity=".85"/>
        <!-- kumaş kırışıklıkları -->
        <g stroke="#1B1F21" stroke-width="1.6" fill="none" opacity=".30">
          <path d="M96 150 Q116 210 100 300"/><path d="M204 150 Q186 214 202 300"/>
          <path d="M86 116 Q104 132 100 158"/><path d="M214 116 Q196 132 200 158"/></g>
        <g stroke="#fff" stroke-width="1.2" fill="none" opacity=".07">
          <path d="M120 190 Q150 200 180 190"/><path d="M114 250 Q150 262 186 250"/></g>
      </svg>
      <div style="position:absolute;left:50%;top:41%;transform:translate(-50%,-50%)">
        {kilit(w*0.145, w*0.082, ink='#F2EFE9', bronz=BRONZ)}</div>
    </div>'''


def sapka(w=190):
    """Kep — ön panelde nakış amblem."""
    return f'''<div style="position:relative;width:{w}px">
      <svg viewBox="0 0 300 210" style="width:100%;height:auto;display:block;
        filter:drop-shadow(0 12px 22px rgba(30,28,25,.32))">
        <defs><linearGradient id="sg" x1="0" y1="0" x2=".3" y2="1">
          <stop offset="0" stop-color="#3E4346"/><stop offset=".5" stop-color="#2E3335"/>
          <stop offset="1" stop-color="#24282A"/></linearGradient></defs>
        <path d="M150 14 C88 14 44 62 42 128 L258 128 C256 62 212 14 150 14 Z" fill="url(#sg)"/>
        <path d="M42 128 C30 168 62 190 128 190 L150 190 L150 128 Z" fill="#262A2C"/>
        <path d="M258 128 C270 168 238 190 172 190 L150 190 L150 128 Z" fill="#2A2E31"/>
        <g stroke="#1C2022" stroke-width="1.8" fill="none" opacity=".55">
          <path d="M150 16 V128"/><path d="M96 26 Q104 78 100 128"/><path d="M204 26 Q196 78 200 128"/></g>
        <ellipse cx="150" cy="14" rx="9" ry="7" fill="#1F2325"/>
      </svg>
      <div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%)">
        {amb(f'{w*0.24:.0f}px', ink='#EFECE6')}</div>
    </div>'''


def kupa(w=170):
    """Seramik kupa — silindir gradyanı, kulp, zemin gölgesi."""
    return f'''<div style="position:relative;width:{w}px">
      <svg viewBox="0 0 260 230" style="width:100%;height:auto;display:block">
        <defs><linearGradient id="kg" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="#D8D3CA"/><stop offset=".14" stop-color="#FBFAF7"/>
          <stop offset=".52" stop-color="#FFFFFF"/><stop offset=".86" stop-color="#EAE6DE"/>
          <stop offset="1" stop-color="#C9C4BB"/></linearGradient>
          <radialGradient id="kgz"><stop offset="0" stop-color="#000" stop-opacity=".26"/>
          <stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>
        <ellipse cx="118" cy="214" rx="86" ry="13" fill="url(#kgz)"/>
        <path d="M196 92 a34 34 0 1 1 0 44 l-14 0 0-44 z" fill="none" stroke="#E4DFD7" stroke-width="15"/>
        <rect x="42" y="46" width="152" height="164" rx="9" fill="url(#kg)"/>
        <ellipse cx="118" cy="48" rx="76" ry="15" fill="#EFEBE4"/>
        <ellipse cx="118" cy="48" rx="66" ry="11" fill="#DAD5CC"/>
      </svg>
      <div style="position:absolute;left:44%;top:53%;transform:translate(-50%,-50%)">
        {amb(f'{w*0.30:.0f}px')}</div>
    </div>'''


def tabela(w=430):
    """Gece bina cephesi — kutu harf, arkadan aydınlatma halesi."""
    h = w * 0.50
    return f'''<div style="width:{w}px;height:{h:.0f}px;position:relative;border-radius:2px;
      background:linear-gradient(180deg,#22262A 0%,#1A1E21 55%,#141719 100%);overflow:hidden;
      box-shadow:0 16px 40px rgba(0,0,0,.32)">
      <div style="position:absolute;inset:0;
        background:repeating-linear-gradient(90deg,transparent 0 {w*0.115:.0f}px,rgba(255,255,255,.028) {w*0.115:.0f}px {w*0.117:.0f}px),
        repeating-linear-gradient(0deg,transparent 0 {h*0.30:.0f}px,rgba(255,255,255,.022) {h*0.30:.0f}px {h*0.305:.0f}px)"></div>
      <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
        filter:drop-shadow(0 0 {w*0.09:.0f}px rgba(184,115,51,.55)) drop-shadow(0 0 {w*0.03:.0f}px rgba(255,236,214,.35))">
        {yatay(w*0.125, w*0.072, ink='#F6F3EE', bronz=BRONZ)}</div>
      <div style="position:absolute;left:0;right:0;bottom:0;height:{h*0.22:.0f}px;
        background:linear-gradient(180deg,transparent,rgba(0,0,0,.5))"></div>
    </div>'''


def telefon(w=175):
    """Instagram profili — cihaz çerçevesi ve ızgara."""
    kare = lambda bg, ic: (f'<div style="aspect-ratio:1;background:{bg};display:flex;'
                           f'align-items:center;justify-content:center;overflow:hidden">{ic}</div>')
    hucre = [kare('#C9C4BA', ''), kare(INK, amb(f'{w*0.13:.0f}px', ink=KAGIT)),
             kare(BRONZ, f'<span style="font-family:Questrial;color:#fff;font-size:{w*0.075:.0f}px">%25</span>'),
             kare('#B9B3A8', ''),
             kare(KAGIT, f'<span style="font-family:Questrial;color:{INK};font-size:{w*0.052:.0f}px;letter-spacing:.2em">GLOBAL</span>'),
             kare('#A9A399', '')]
    return f'''<div style="width:{w}px;border-radius:{w*0.115:.0f}px;background:#1A1D1F;
      padding:{w*0.028:.0f}px;box-shadow:0 3px 6px rgba(0,0,0,.25),0 18px 40px rgba(0,0,0,.30)">
      <div style="background:{KAGIT};border-radius:{w*0.092:.0f}px;overflow:hidden">
        <div style="height:{w*0.055:.0f}px;background:#1A1D1F"></div>
        <div style="padding:{w*0.055:.0f}px;display:flex;gap:{w*0.05:.0f}px;align-items:center">
          <div style="width:{w*0.20:.0f}px;height:{w*0.20:.0f}px;border-radius:50%;background:{INK};
            display:flex;align-items:center;justify-content:center">{amb(f'{w*0.115:.0f}px', ink=KAGIT)}</div>
          <div style="font-family:Inter;font-size:{w*0.045:.0f}px">
            <b>globalyapi</b><div style="color:#8C8880;font-size:{w*0.038:.0f}px">Yapı Geliştirme</div></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:{w*0.012:.0f}px">{''.join(hucre)}</div>
      </div></div>'''


def ekran(w=430):
    """Masaüstü web — tarayıcı çerçevesi, kahraman alan."""
    return f'''<div style="width:{w}px;border-radius:{w*0.014:.0f}px;overflow:hidden;
      box-shadow:0 3px 8px rgba(40,36,32,.18),0 20px 46px rgba(40,36,32,.24)">
      <div style="background:#E4E0D9;padding:{w*0.016:.0f}px {w*0.022:.0f}px;display:flex;
        gap:{w*0.011:.0f}px;align-items:center">
        <span style="width:{w*0.016:.0f}px;height:{w*0.016:.0f}px;border-radius:50%;background:#D8695B"></span>
        <span style="width:{w*0.016:.0f}px;height:{w*0.016:.0f}px;border-radius:50%;background:#DDB05A"></span>
        <span style="width:{w*0.016:.0f}px;height:{w*0.016:.0f}px;border-radius:50%;background:#93B87E"></span>
        <span style="flex:1;text-align:center;font-family:Inter;font-size:{w*0.020:.0f}px;
          color:#8C8880;background:#F2EFE9;border-radius:{w*0.008:.0f}px;padding:{w*0.006:.0f}px">globalyapi.com.tr</span>
      </div>
      <div style="background:{KAGIT}">
        <div style="padding:{w*0.030:.0f}px {w*0.042:.0f}px;display:flex;justify-content:space-between;
          align-items:center;border-bottom:1px solid #E4E0D9">
          {yatay(w*0.052, w*0.030)}
          <div style="font-family:Inter;font-size:{w*0.021:.0f}px;letter-spacing:.14em;color:#6A665F;
            display:flex;gap:{w*0.035:.0f}px">
            <span>PROJELER</span><span>KURUMSAL</span><span>YATIRIM</span><span>İLETİŞİM</span></div>
        </div>
        <div style="background:linear-gradient(160deg,#2E3335,#23272A);padding:{w*0.075:.0f}px {w*0.042:.0f}px;
          position:relative;overflow:hidden">
          <div style="position:absolute;right:{-w*0.04:.0f}px;bottom:{-w*0.05:.0f}px;opacity:.10">
            {amb(f'{w*0.32:.0f}px', ink=KAGIT)}</div>
          <div style="font-family:Inter;font-size:{w*0.019:.0f}px;letter-spacing:.24em;color:{BRONZ}">
            İZMİT · YENİ ETAP</div>
          <div style="font-family:Questrial;font-size:{w*0.055:.0f}px;color:{KAGIT};
            line-height:1.22;margin:{w*0.022:.0f}px 0 {w*0.030:.0f}px">
            Şehrin merkezinde,<br>geleceğin değeri.</div>
          <span style="font-family:Inter;font-size:{w*0.021:.0f}px;background:{BRONZ};color:#fff;
            padding:{w*0.017:.0f}px {w*0.032:.0f}px;letter-spacing:.10em">PROJEYİ İNCELE</span>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:{w*0.020:.0f}px;padding:{w*0.030:.0f}px {w*0.042:.0f}px">
          {'<div style="aspect-ratio:4/3;background:linear-gradient(150deg,#D4CFC5,#C2BCB1)"></div>' * 3}
        </div></div></div>'''


# ═══════════════════════════════════════════════════ SAYFALAR
CSS = f'''
@page{{size:594mm 420mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Inter,sans-serif;color:{INK};background:#888}}
.page{{width:594mm;height:420mm;position:relative;overflow:hidden;
  page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto}}
.pad{{position:absolute;inset:0;padding:26mm 30mm}}
.ust{{display:flex;justify-content:space-between;font-size:9pt;letter-spacing:.20em;
  color:{GRI};margin-bottom:18mm}}
h2{{font-family:Questrial;font-size:30pt;letter-spacing:-.01em;font-weight:400;margin-bottom:3mm}}
p.alt{{font-size:11pt;color:{GRI};margin-bottom:14mm;max-width:180mm;line-height:1.6}}
.dip{{position:absolute;left:30mm;right:30mm;bottom:16mm;display:flex;
  justify-content:space-between;font-size:8pt;letter-spacing:.20em;color:{GRI}}}
.kutu{{background:#fff;border:1px solid #E4E0D9;padding:14mm;display:flex;
  flex-direction:column;align-items:center;justify-content:center;gap:8mm}}
.kutu .et{{font-size:8pt;letter-spacing:.20em;color:{GRI};text-align:center}}
.sahne{{{SAHNE};display:flex;align-items:center;justify-content:center;padding:16mm}}
.g2{{display:grid;grid-template-columns:1fr 1fr;gap:8mm}}
.g3{{display:grid;grid-template-columns:repeat(3,1fr);gap:8mm}}
.g4{{display:grid;grid-template-columns:repeat(4,1fr);gap:8mm}}
table{{width:100%;border-collapse:collapse;font-size:9.5pt}}
th{{text-align:left;font-size:8pt;letter-spacing:.18em;color:{GRI};padding:0 0 3mm;
  border-bottom:1px solid {INK};font-weight:400}}
td{{padding:3mm 0;border-bottom:1px solid #E4E0D9;color:#5A5650}}
td.k{{color:{INK}}}
'''


def s01():
    return f'''<section class="page" style="background:{INK}">
      <div style="position:absolute;inset:0;
        background:repeating-linear-gradient(90deg,transparent 0 40mm,rgba(255,255,255,.02) 40mm 40.3mm),
        repeating-linear-gradient(0deg,transparent 0 40mm,rgba(255,255,255,.02) 40mm 40.3mm)"></div>
      <div class="pad" style="display:flex;flex-direction:column;justify-content:center;align-items:center">
        {kilit(210, 84, ink=KAGIT, bronz=BRONZ)}
        <div style="width:26mm;height:1px;background:{BRONZ};margin:22mm 0 8mm"></div>
        <div style="font-family:Inter;font-size:10pt;letter-spacing:.34em;color:{GRI}">
          MARKA KİMLİĞİ REHBERİ</div>
      </div>
      <div class="dip" style="color:#6E6A64"><span>V2.0 — AĞUSTOS 2026</span>
        <span>BAKIR BRONZ · QUESTRIAL</span></div></section>'''


def s02():
    k = lambda et, ic, bg='#fff': (f'<div class="kutu" style="background:{bg}">'
                                   f'<div style="flex:1;display:flex;align-items:center">{ic}</div>'
                                   f'<div class="et">{et}</div></div>')
    ic = f'''<div class="g3" style="height:264mm">
      {k('DİKEY — ANA KİLİT', kilit(104, 38))}
      {k('YATAY — ANTET, WEB', yatay(76, 32))}
      {k('AMBLEM — FAVICON, NAKIŞ', amb('76mm'))}
      {k('ROZET — MÜHÜR', f'<div style="width:74mm;height:74mm;border:2pt solid {INK};border-radius:50%;display:flex;align-items:center;justify-content:center">{amb("38mm")}</div>')}
      {k('NEGATİF — KOYU ZEMİN', kilit(90, 34, ink=KAGIT, bronz=BRONZ), INK)}
      {k('TEK RENK — KAŞE, GRAVÜR', kilit(90, 34, ink=INK, bronz=INK))}
    </div>'''
    return sayfa('01', 'LOGO', 'Logo yapısı ve kilit versiyonları',
                 'Amblem "G" harfini ev kesitiyle birleştirir. Çatı yüksekliği v2.0\'da '
                 'kısaltıldı; amblem kilit içinde küçültülerek logotype ile dengelendi.', ic)


def s03():
    r = [('Ana Renk', INK, '#2F3336', 'C78 M64 Y58 K52', 'PANTONE 432 C', 'Amblem, logotype, koyu zeminler'),
         ('Bakır Bronz', BRONZ, '#B87333', 'C24 M58 Y88 K9', 'PANTONE 876 C · RAL 8001', 'Vurgu — amblem detay, alt satır'),
         ('Nötr Gri', GRI, '#A6A39A', 'C34 M30 Y34 K0', 'PANTONE 415 C', 'İkincil metin, ayraçlar'),
         ('Kağıt', KAGIT, '#F5F3F0', 'C3 M3 Y5 K0', '—', 'Zemin ve açık yüzeyler')]
    kart = ''.join(f'''<div style="background:#fff;border:1px solid #E4E0D9">
        <div style="height:132mm;background:{h}"></div>
        <div style="padding:8mm">
          <div style="font-family:Questrial;font-size:19pt;margin-bottom:5mm">{ad}</div>
          <div style="font-size:9pt;line-height:2;color:#5A5650">{kod}<br>{cmyk}<br>
            <span style="color:{BRONZ}">{pan}</span></div>
          <div style="font-size:8.5pt;color:{GRI};margin-top:4mm;line-height:1.5">{kul}</div>
        </div></div>''' for ad, h, kod, cmyk, pan, kul in r)
    kom = [('Kağıt üzerine koyu', KAGIT, INK, BRONZ, 'Birincil — evrak, katalog'),
           ('Koyu üzerine kağıt', INK, KAGIT, BRONZ, 'Kapak, tabela, dijital kahraman'),
           ('Bronz üzerine kağıt', BRONZ, '#FFFFFF', '#FFFFFF', 'Yalnız eylem alanı, küçük yüzey'),
           ('Nötr üzerine koyu', GRI, INK, INK, 'Ayraç ve ikincil bloklar')]
    kombin = ''.join(f'''<div style="background:{z};display:flex;flex-direction:column;
        justify-content:center;align-items:center;gap:4mm;border:1px solid #E4E0D9">
        <div style="font-family:Questrial;font-size:17pt;letter-spacing:.24em;color:{y}">GLOBAL</div>
        <div style="font-size:8pt;letter-spacing:.20em;color:{v}">{ad}</div>
        <div style="font-size:7.5pt;color:{y};opacity:.55">{n}</div></div>'''
        for ad, z, y, v, n in kom)
    ic = f'''<div class="g4">{kart}</div>
      <div style="margin-top:16mm;display:flex;height:16mm">
        <div style="flex:60;background:{INK}"></div><div style="flex:25;background:{KAGIT};border:1px solid #E4E0D9"></div>
        <div style="flex:10;background:{BRONZ}"></div><div style="flex:5;background:{GRI}"></div></div>
      <div style="font-size:10pt;color:{GRI};margin-top:5mm">
        Oran: koyu zemin %60 · kağıt %25 · bronz %10 · nötr %5. Bronz her zaman vurgudur, zemin olmaz.</div>
      <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin:16mm 0 6mm">ZEMİN KOMBİNASYONLARI</div>
      <div class="g4" style="height:62mm">{kombin}</div>'''
    return sayfa('02', 'RENK', 'Bakır Bronz paleti',
                 'Ana yön. Metalik uygulamalarda folyo ve RAL karşılıkları aşağıdadır.', ic)


def s04():
    md = [('Sayfa başlığı', 'Questrial', '30 pt / -1%', 30, 'Questrial', '0'),
          ('Alt başlık', 'Questrial', '18 pt / 0', 18, 'Questrial', '0'),
          ('Gövde metni', 'Inter Regular', '11 pt / 0', 11, 'Inter', '0'),
          ('Etiket / üst bant', 'Inter Medium', '8 pt / +20%', 8, 'Inter', '.20em'),
          ('Teknik veri', 'IBM Plex Mono', '10 pt / +5%', 10, 'IBM Plex Mono', '.05em')]
    merdiven = ''.join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td>'
                       f'<td style="font-family:{f};font-size:{sz}pt;letter-spacing:{ls}">'
                       f'Yaşanabilir yapılar</td></tr>' for a, b, c, sz, f, ls in md)
    ic = f'''<div style="max-width:440mm">
      <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin-bottom:5mm">LOGOTYPE — QUESTRIAL · +240</div>
      <div style="font-family:Questrial;font-size:66pt;letter-spacing:.24em;margin-bottom:26mm">GLOBAL</div>
      <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin-bottom:5mm">BAŞLIK — QUESTRIAL</div>
      <div style="font-family:Questrial;font-size:38pt;margin-bottom:26mm">Yaşanabilir yapılar, ölçülebilir değer</div>
      <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin-bottom:5mm">METİN — INTER REGULAR</div>
      <div style="font-size:18pt;line-height:1.75;margin-bottom:26mm;max-width:330mm">
        Global Yapı Geliştirme A.Ş., arsa geliştirmeden anahtar teslime kadar süreci
        tek elden yürütür. ğ ı İ ş Ş ç Ö Ü</div>
      <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin-bottom:5mm">TEKNİK — IBM PLEX MONO</div>
      <div style="font-family:'IBM Plex Mono',monospace;font-size:21pt;letter-spacing:.05em">
        BLOK A-12 · 3+1 · 148 M² · TESLİM 2027 Q2</div>
      <div style="font-size:9.5pt;color:{GRI};margin-top:16mm;line-height:1.6">
        Harf çiftleri: büyük harf + geniş espas kurumsaldır; küçük harf yalnızca uzun metinde kullanılır.</div>
      <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin:18mm 0 7mm">ÖLÇEK MERDİVENİ</div>
      <table style="max-width:430mm"><tr><th>Kullanım</th><th>Yazı tipi</th><th>Boyut / espas</th><th>Örnek</th></tr>
        {merdiven}</table>
    </div>'''
    return sayfa('03', 'TİPOGRAFİ', 'Yazı ailesi',
                 'Questrial tek ağırlıkta; hiyerarşi boyut ve espasla kurulur.', ic)


def s05():
    ic = f'''<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:9mm;height:266mm">
      <div class="sahne" style="flex-direction:column;gap:10mm">
        <div>{zarf(780)}</div>
        <div class="et" style="font-size:8pt;letter-spacing:.20em;color:#78736B">
          MEKTUP ZARFI — DL 220×110 MM · LOGO GENİŞLİĞİ 70 MM</div>
      </div>
      <div style="display:grid;grid-template-rows:1fr 1fr;gap:8mm">
        <div class="sahne">{antetli(268)}</div>
        <div class="sahne">{kartvizit(340)}</div>
      </div></div>
      <div class="g3" style="margin-top:8mm;font-size:9pt;color:{GRI}">
        <div><b style="color:{INK}">Zarf</b> — logo sol üst, gönderici arka kapaktadır.</div>
        <div><b style="color:{INK}">Antet</b> — A4 210×297 mm; bronz çizgi başlığı gövdeden ayırır.</div>
        <div><b style="color:{INK}">Kartvizit</b> — 85×54 mm; ön koyu, arka kağıt.</div></div>'''
    return sayfa('04', 'KURUMSAL EVRAK', 'Zarf · Antet · Kartvizit',
                 'Üretim ölçüleri etiketlerde. Baskıda bronz, folyo yaldız veya tek renk '
                 'ofset olarak uygulanabilir.', ic)


def s06():
    ic = f'''<div class="g2" style="height:274mm">
      <div class="sahne" style="flex-direction:column;gap:9mm;background:#1A1E21">
        {tabela(820)}
        <div style="font-size:8pt;letter-spacing:.20em;color:#8C8880">
          BİNA TABELASI — KUTU HARF, ARKADAN AYDINLATMA · YÜKSEKLİK 60 CM</div>
      </div>
      <div class="sahne" style="flex-direction:column;gap:9mm">
        <div style="position:relative;width:760px;height:430px;
          background:linear-gradient(180deg,#DCD7CE 0%,#CFC9BF 62%,#C4BEB3 100%);overflow:hidden">
          <div style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);
            width:490px;height:275px;background:linear-gradient(170deg,#F0ECE4,#E2DDD3);
            box-shadow:0 18px 34px rgba(40,36,32,.28)">
            <div style="position:absolute;left:-38px;right:-38px;top:-76px;height:110px;
              background:linear-gradient(180deg,#33383B,#2A2E31);
              clip-path:polygon(9% 100%,50% 0,91% 100%)"></div>
            <div style="position:absolute;left:32px;bottom:34px;width:74px;height:138px;
              background:#2F3336"></div>
            <div style="position:absolute;right:38px;bottom:62px;width:150px;height:100px;
              background:#CFE0E4;border:7px solid #EDE9E1"></div>
            <div style="position:absolute;left:50%;top:44px;transform:translateX(-50%)">
              {amb('62px')}</div>
          </div>
          <div style="position:absolute;left:0;right:0;bottom:0;height:44px;
            background:linear-gradient(180deg,transparent,rgba(90,84,76,.30))"></div>
        </div>
        <div style="font-size:8pt;letter-spacing:.20em;color:#78736B">
          TINY HOUSE — CEPHE APLİKESİ: AMBLEM 40 CM, PASLANMAZ + BRONZ</div>
      </div></div>
      <div style="font-size:9.5pt;color:{GRI};margin-top:7mm;line-height:1.6">
        Tabela montajında logo genişliği cephe genişliğinin %55'ini geçmez. Geceleri yalnız harfler ışır;
        zemin ışımaz. Tiny house ürünlerinde amblem giriş cephesinin üst üçgeninde (alınlık) konumlanır.</div>'''
    return sayfa('05', 'MEKÂN', 'Tabela · Tiny House',
                 'Tabelada kutu harf + arkadan aydınlatma; tiny house cephesinde amblem '
                 'kalıcı metal aplike.', ic)


def s07():
    ic = f'''<div class="g2" style="height:274mm">
      <div class="sahne" style="flex-direction:column;gap:9mm">{tisort(440)}
        <div style="font-size:8pt;letter-spacing:.20em;color:#78736B">
          TİŞÖRT (ARKA) — SERİGRAFİ · LOGO GENİŞLİĞİ 24 CM · YAKA ALTI 8 CM</div></div>
      <div class="sahne" style="flex-direction:column;gap:9mm">{sapka(410)}
        <div style="font-size:8pt;letter-spacing:.20em;color:#78736B">
          ŞAPKA — NAKIŞ · AMBLEM YÜKSEKLİĞİ 5,5 CM · ÖN PANEL ORTASI</div></div></div>
      <div style="font-size:9.5pt;color:{GRI};margin-top:7mm">
        Giyimde wordmark tek başına kullanılmaz; ya tam dikey kilit (tişört) ya yalnız amblem (şapka, yaka).
        Kumaş koyu ise logo negatif, açık ise standart renklidir.</div>'''
    return sayfa('06', 'GİYİM', 'Tişört · Şapka',
                 'Tişörtte baskı arka yakadadır. Şapkada yalnız amblem nakışı kullanılır.', ic)


def s08():
    urun = [('KUPA · SERAMİK', kupa(330), 'Amblem 45 mm', 'Çift renk seramik transfer'),
            ('SULUK · LAZER + BOYA', f'''<div style="width:140px;height:364px;border-radius:38px;
        background:linear-gradient(100deg,#3A3F42,#24282A 55%,#191C1E);position:relative;
        box-shadow:0 14px 26px rgba(30,28,25,.3)">
        <div style="position:absolute;left:50%;top:22px;transform:translateX(-50%);width:76px;
          height:32px;border-radius:10px;background:#15181A"></div>
        <div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%)">
          {amb('58px', ink='#EFECE6')}</div></div>''', 'Dikey kilit 40 mm', 'Lazer gravür + boya dolgu'),
            ('ANAHTARLIK · DERİ', f'''<div style="width:172px;height:276px;border-radius:14px;
        background:linear-gradient(150deg,#C98A44,#B87333 55%,#96601F);position:relative;
        box-shadow:0 12px 22px rgba(60,40,15,.34)">
        <div style="position:absolute;left:50%;top:22px;transform:translateX(-50%);width:32px;
          height:32px;border-radius:50%;border:6px solid #E7E3DB"></div>
        <div style="position:absolute;left:50%;top:56%;transform:translate(-50%,-50%)">
          {amb('82px', ink='#3A2A12')}</div></div>''', 'Amblem 22 mm', 'Sıcak gofre')]
    kutu = ''.join(f'''<div class="sahne" style="flex-direction:column;gap:8mm;padding:12mm">
        <div style="flex:1;display:flex;align-items:center">{ic}</div>
        <div style="font-size:8pt;letter-spacing:.18em;color:#78736B;text-align:center">{et}</div>
      </div>''' for et, ic, _, _ in urun)
    satir = ''.join(f'<tr><td class="k">{et.split(" · ")[0].title()}</td><td>{o}</td><td>{t}</td></tr>'
                    for et, _, o, t in urun)
    ic = f'''<div class="g3" style="height:236mm">{kutu}</div>
      <table style="margin-top:12mm"><tr><th>Ürün</th><th>Logo ölçüsü</th><th>Teknik</th></tr>{satir}</table>
      <div style="font-size:9.5pt;color:{GRI};margin-top:7mm">
        Silindirik ürünlerde baskı alanı çevre uzunluğunun üçte birini geçmez; logo daima kulba göre ortalanır.</div>'''
    return sayfa('07', 'ÜRÜNLER', 'Kupa · Suluk · Anahtarlık',
                 'Küçük yüzeylerde yalnız amblem; silindirik yüzeylerde dikey kilit kullanılır.', ic)


def s09():
    ic = f'''<div style="display:grid;grid-template-columns:auto 1fr;gap:16mm;height:272mm;align-items:center">
      <div class="sahne" style="padding:14mm">{telefon(400)}</div>
      <div class="sahne" style="padding:14mm">{ekran(920)}</div></div>
      <div class="g2" style="margin-top:8mm;font-size:9.5pt;color:{GRI}">
        <div><b style="color:{INK}">Instagram</b> — profil fotoğrafı amblemdir, asla wordmark içermez.
          Izgara düzeni: proje karesi → koyu bilgi karesi → bronz vurgu.</div>
        <div><b style="color:{INK}">Web</b> — menü sabit ve açık zeminli; kahraman görselde başlık
          Questrial, eylem düğmesi bronzdur.</div></div>'''
    return sayfa('08', 'DİJİTAL', 'Sosyal medya · Web sitesi',
                 'Küçük dairede yalnız amblem okunur; profil fotoğrafı bu yüzden rozet formundadır.', ic)


def s10():
    ic = f'''<div class="g2" style="height:262mm">
      <div>
        <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin-bottom:6mm">KORUMA ALANI</div>
        <div style="background:#fff;border:1px solid #E4E0D9;padding:16mm;position:relative">
          <div style="border:1px dashed {BRONZ};padding:30mm;display:flex;justify-content:center">
            {kilit(96, 34)}</div>
          <div style="font-size:9pt;color:{GRI};margin-top:8mm;line-height:1.6">
            Logonun her yönünde, amblem yüksekliğinin yarısı kadar boş alan bırakılır.
            Bu alana metin, görsel veya kenarlık giremez.</div>
        </div>
        <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin:10mm 0 6mm">EN KÜÇÜK ÖLÇÜ</div>
        <div style="background:#fff;border:1px solid #E4E0D9;padding:12mm;display:flex;
          gap:22mm;align-items:flex-end;justify-content:center">
          <div style="text-align:center">{kilit(44, 16)}
            <div style="font-size:8pt;color:{GRI};margin-top:6mm">BASKI 25 MM</div></div>
          <div style="text-align:center">{amb('22mm')}
            <div style="font-size:8pt;color:{GRI};margin-top:6mm">EKRAN 32 PX</div></div>
        </div>
      </div>
      <div>
        <div style="font-size:8.5pt;letter-spacing:.20em;color:{GRI};margin-bottom:6mm">YAPILMAZ</div>
        <div class="g2" style="gap:6mm">
          {''.join(f"""<div style="background:#fff;border:1px solid #E4E0D9;padding:9mm;text-align:center">
            <div style="height:46mm;display:flex;align-items:center;justify-content:center;{st}">
              {amb('30mm')}</div>
            <div style="font-size:8.5pt;color:{BRONZ};margin-top:5mm">{ad}</div></div>"""
            for ad, st in [('Orantısız ölçekleme','transform:scaleX(1.5)'),
                           ('Döndürme','transform:rotate(-14deg)'),
                           ('Gölge / efekt','filter:drop-shadow(0 6px 5px rgba(0,0,0,.5))'),
                           ('Palet dışı renk','filter:hue-rotate(115deg) saturate(2.2)')])}
        </div>
        <div style="font-size:9.5pt;color:{GRI};margin-top:8mm;line-height:1.7">
          Amblem yalnız bu rehberde tanımlı biçimlerde kullanılır. Renk değişikliği, efekt,
          çerçeve içine alma ve oran bozma marka bütünlüğünü kırar.</div>
      </div></div>'''
    return sayfa('09', 'KULLANIM', 'Koruma alanı · En küçük ölçü · Yapılmaz',
                 'Bu sayfa bağlayıcıdır; tedarikçi ve ajanslara logo ile birlikte iletilir.', ic)


def s11():
    return f'''<section class="page" style="background:{INK}">
      <div class="pad" style="display:flex;flex-direction:column;justify-content:center;align-items:center">
        {kilit(170, 66, ink=KAGIT, bronz=BRONZ)}
        <div style="width:26mm;height:1px;background:{BRONZ};margin:20mm 0 10mm"></div>
        <div style="font-size:9pt;letter-spacing:.24em;color:{GRI};text-align:center;line-height:2.4">
          TESLİM SETİ: LOGO-DİKEY.SVG · YATAY.SVG · AMBLEM.SVG · NEGATİF.SVG · TEKRENK.SVG<br>
          BU REHBER TÜM UYGULAMALARDA BAĞLAYICIDIR · SORULAR: MARKA@GLOBALYAPI.COM.TR</div>
      </div></section>'''


def belge():
    link = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Questrial&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=block">')
    sayfalar = ''.join(f() for f in (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11))
    return f'<meta charset="utf-8"><title>GLOBAL Marka Kimliği</title>{link}<style>{CSS}</style>{DOKU}{sayfalar}'


if __name__ == '__main__':
    yol = os.path.join(BASE, 'kimlik.html')
    open(yol, 'w', encoding='utf-8').write(belge())
    print('yazıldı:', yol)
