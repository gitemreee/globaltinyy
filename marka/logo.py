#!/usr/bin/env python3
"""
GLOBAL YAPI GELİŞTİRME A.Ş. — wordmark üreteci.

Harfler fontla dizilmez, geometrik olarak çizilir (monoline sans).
İki mimari detay ince ikincil çizgiyle anlatılır:
  A → çatı saçağı (gable eave)
  O → dörtlü pencere kayıtları (aynı zamanda meridyen/ekvator iması)

Kullanım:  python3 marka/logo.py
Çıktı:     marka/svg/*.svg  +  marka/onizleme.html
"""
import os, math

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg')
os.makedirs(OUT, exist_ok=True)

CAP = 100.0          # büyük harf yüksekliği
R   = 44.0           # yuvarlak harf yarıçapı
A_W = 76.0           # A genişliği
A_APEX = A_W / 2
A_BAR = 68.0         # A ortası çubuk yüksekliği
A_EAVE = 26.0        # çatı saçağı yüksekliği
A_OVER = 11.0        # saçak taşması
L_W = 58.0
B_BOWL = 25.0
B_STEM = 28.0


def p(v):
    """Kısa sayı biçimi."""
    return f"{v:.2f}".rstrip('0').rstrip('.')


# ---------------------------------------------------------------- harfler
def glyph_G():
    a = math.radians(-35)
    x1, y1 = R + R * math.cos(a), 50 + R * math.sin(a)
    d = f"M {p(x1)} {p(y1)} A {p(R)} {p(R)} 0 1 0 {p(2*R)} 50 H {p(R - 2)}"
    return {'w': 2 * R, 'main': [d], 'thin': []}


def glyph_L():
    return {'w': L_W, 'main': [f"M 0 0 V {p(CAP)} H {p(L_W)}"], 'thin': []}


def glyph_O(w, pencere=False):
    """Halka. pencere=True ise dörtlü pencere kayıtları eklenir (ince çizgi)."""
    inner = R - w / 2
    main = [f"M 0 50 A {p(R)} {p(R)} 0 1 1 {p(2*R)} 50 A {p(R)} {p(R)} 0 1 1 0 50 Z"]
    thin = [
        f"M {p(R)} {p(50 - inner)} V {p(50 + inner)}",      # dikey kayıt
        f"M {p(R - inner)} 50 H {p(R + inner)}",            # yatay kayıt
    ] if pencere else []
    return {'w': 2 * R, 'main': main, 'thin': thin}


def glyph_B():
    bw = B_STEM + B_BOWL
    return {'w': bw, 'main': [
        f"M 0 0 V {p(CAP)}",
        f"M 0 0 H {p(B_STEM)} A {p(B_BOWL)} {p(B_BOWL)} 0 0 1 {p(B_STEM)} 50 H 0",
        f"M 0 50 H {p(B_STEM)} A {p(B_BOWL)} {p(B_BOWL)} 0 0 1 {p(B_STEM)} {p(CAP)} H 0",
    ], 'thin': []}


def glyph_A(cati='sacak'):
    """Çatılı A.

    cati='sacak'  → orta çubuk yerinde durur, üstte ince saçak çizgisi
    cati='kiris'  → orta çubuğun kendisi iki yana taşarak saçak olur (tek çizgi)
    """
    def lx(y): return A_APEX * (1 - y / CAP)          # sol eğik
    def rx(y): return A_APEX + A_APEX * (y / CAP)     # sağ eğik
    diag = f"M 0 {p(CAP)} L {p(A_APEX)} 0 L {p(A_W)} {p(CAP)}"
    if cati == 'yalin':
        # Saf çatı: yatay çubuk yok, sadece iki eğik.
        return {'w': A_W, 'main': [diag], 'thin': []}
    if cati == 'kiris':
        y = 60.0
        over = 13.0
        return {'w': A_W, 'main': [
            diag,
            f"M {p(lx(y) - over)} {p(y)} H {p(rx(y) + over)}",
        ], 'thin': []}
    y = 40.0                                          # saçak: daha aşağı, daha uzun
    over = 15.0
    return {'w': A_W, 'main': [
        diag,
        f"M {p(lx(A_BAR))} {p(A_BAR)} H {p(rx(A_BAR))}",
    ], 'thin': [f"M {p(lx(y) - over)} {p(y)} H {p(rx(y) + over)}"]}


# ---------------------------------------------------------------- dizgi
# Optik kerning: yuvarlak ve köşegen harflerin yan boşlukları göz için düzeltilir.
KERN = {('G','L'): -3, ('L','O'): -15, ('O','B'): -7, ('B','A'): 3, ('A','L'): -5}


def wordmark(w=13.0, track=28.0, thin_ratio=0.62, ink='#1A1A18', cati='yalin', pencere=False):
    """GLOBAL kelimesini tek <g> olarak döndürür; (svg_parcasi, genislik)."""
    seq = [('G', glyph_G()), ('L', glyph_L()), ('O', glyph_O(w, pencere)),
           ('B', glyph_B()), ('A', glyph_A(cati)), ('L', glyph_L())]
    glyphs = [g for _, g in seq]
    names = [n for n, _ in seq]
    tw = max(w * thin_ratio, 3.2)
    parts, x = [], 0.0
    for i, gl in enumerate(glyphs):
        body = ''.join(
            f'<path d="{d}" stroke-width="{p(w)}"/>' for d in gl['main']
        ) + ''.join(
            f'<path d="{d}" stroke-width="{p(tw)}"/>' for d in gl['thin']
        )
        parts.append(f'<g transform="translate({p(x)},0)">{body}</g>')
        x += gl['w'] + track
        if i + 1 < len(glyphs):
            x += KERN.get((names[i], names[i + 1]), 0)
    total = x - track
    g = (f'<g fill="none" stroke="{ink}" stroke-linecap="square" '
         f'stroke-linejoin="miter" stroke-miterlimit="10">' + ''.join(parts) + '</g>')
    return g, total


def lockup(w=13.0, track=28.0, ink='#1A1A18', desc_ink=None, stacked=False, cati='yalin', pencere=False,
           desc='YAPI GELİŞTİRME A.Ş.'):
    """Wordmark + açıklama satırı. Tam SVG belgesi döndürür."""
    desc_ink = desc_ink or ink
    mark, mw = wordmark(w, track, ink=ink, cati=cati, pencere=pencere)
    pad = w / 2 + 2
    ds = 15.0                      # açıklama punto
    gap = 26.0                     # kelime ile açıklama arası
    if stacked:
        h = CAP + gap + ds + pad * 2
        body = (f'<g transform="translate({p(pad)},{p(pad)})">{mark}'
                f'<text x="{p(mw/2 - ds*0.17)}" y="{p(CAP + gap)}" text-anchor="middle" '
                f'font-family="Liberation Sans, Arial, Helvetica, sans-serif" '
                f'font-size="{p(ds)}" letter-spacing="{p(ds*0.34)}" '
                f'fill="{desc_ink}">{desc}</text></g>')
        vw = mw + pad * 2 + ds * 0.34
    else:
        h = CAP + gap + ds + pad * 2
        body = (f'<g transform="translate({p(pad)},{p(pad)})">{mark}'
                f'<text x="0" y="{p(CAP + gap)}" '
                f'font-family="Liberation Sans, Arial, Helvetica, sans-serif" '
                f'font-size="{p(ds)}" letter-spacing="{p(ds*0.34)}" '
                f'fill="{desc_ink}">{desc}</text></g>')
        vw = mw + pad * 2 + ds * 0.34
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {p(vw)} {p(h)}" '
            f'width="{p(vw)}" height="{p(h)}">{body}</svg>')


def amblem(kind='cephe', w=13.0, ink='#1A1A18', cati='yalin'):
    """Amblem. 'cephe' = çatı + pencere birleşik; 'pencere' (O); 'cati' (A)."""
    pad = w / 2 + 4
    if kind == 'cephe':
        gl = _amblem_cephe(w)
    elif kind == 'pencere':
        gl = glyph_O(w, pencere=True)
    else:
        gl = glyph_A(cati)
    tw = max(w * 0.62, 3.2)
    body = ''.join(f'<path d="{d}" stroke-width="{p(w)}"/>' for d in gl['main']) + \
           ''.join(f'<path d="{d}" stroke-width="{p(tw)}"/>' for d in gl['thin'])
    vw, vh = gl['w'] + pad * 2, CAP + pad * 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {p(vw)} {p(vh)}" '
            f'width="{p(vw)}" height="{p(vh)}">'
            f'<g fill="none" stroke="{ink}" stroke-linecap="square" stroke-miterlimit="10" '
            f'transform="translate({p(pad)},{p(pad)})">{body}</g></svg>')


def _amblem_cephe(w):
    """Çatı + altında dörtlü pencere — bir ev cephesi işareti."""
    W = 96.0
    roof = f"M 0 46 L {p(W/2)} 2 L {p(W)} 46"      # saçaklı gable
    pr = 21.0                                       # pencere yarıçapı
    pcy = 74.0
    inner = pr - w / 2
    ring = (f"M {p(W/2 - pr)} {p(pcy)} A {p(pr)} {p(pr)} 0 1 1 {p(W/2 + pr)} {p(pcy)} "
            f"A {p(pr)} {p(pr)} 0 1 1 {p(W/2 - pr)} {p(pcy)} Z")
    thin = [f"M {p(W/2)} {p(pcy - inner)} V {p(pcy + inner)}",
            f"M {p(W/2 - inner)} {p(pcy)} H {p(W/2 + inner)}"]
    return {'w': W, 'main': [roof, ring], 'thin': thin}


# ---------------------------------------------------------------- konseptler
INK, PAPER, TAN = '#1A1A18', '#FBFAF7', '#C3B4A0'
KONSEPT = {
    'k1-ince':  dict(w=9.0,  track=34.0),
    'k2-orta':  dict(w=13.0, track=28.0),
    'k3-kalin': dict(w=18.0, track=22.0),
}

# Onaylanan yön: K2 orta ağırlık, A saf çatı, O sade daire.
FINAL = KONSEPT['k2-orta']

if __name__ == '__main__':
    def yaz(fn, svg):
        open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(svg)
        return fn

    files = []
    for tag, ink in (('siyah', INK), ('beyaz', '#FFFFFF'), ('greige', TAN)):
        files.append(yaz(f'logo-yatay-{tag}.svg', lockup(ink=ink, **FINAL)))
        files.append(yaz(f'logo-dikey-{tag}.svg', lockup(ink=ink, stacked=True, **FINAL)))
        mark, _ = wordmark(ink=ink, **FINAL)
        files.append(yaz(f'wordmark-{tag}.svg',
                         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 112" '
                         f'width="640" height="112"><g transform="translate(7,6)">{mark}</g></svg>'))
        for kind in ('cephe', 'pencere', 'cati'):
            files.append(yaz(f'amblem-{kind}-{tag}.svg', amblem(kind, ink=ink)))
    # Favicon: 16-32 px'te ayakta kalsın diye çizgiler kalınlaştırıldı.
    files.append(yaz('favicon.svg', amblem('cephe', w=17.0)))
    print(f'{len(files)} SVG yazıldı → {OUT}')
