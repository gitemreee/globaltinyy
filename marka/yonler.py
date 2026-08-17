#!/usr/bin/env python3
"""
GLOBAL — üç farklı marka yönü (v4).

İlk denemenin sorunu: amblem jenerikti (çatı+daire her yerde var) ve
wordmark bir imza taşımıyordu. Bu üç yön farklı fikirlerden gider.

Y1 MİMARİ      Ağır, kesme uçlu harfler. Güç ve üretim.
Y2 ÇATI ÇİZGİSİ Kelimenin üstünden geçen saçak; yapı GLOBAL'i örter.
Y3 G MONOGRAM   İmzayı G taşır; kare içinde çatıya dönüşen G.
"""
import os, math

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg-yonler')
os.makedirs(OUT, exist_ok=True)
CAP, R, L_W = 100.0, 44.0, 58.0
A_W, B_BOWL, B_STEM = 76.0, 25.0, 28.0
INK, PAPER, TAN = '#1A1A18', '#FBFAF7', '#C3B4A0'


def p(v): return f"{v:.2f}".rstrip('0').rstrip('.')


# ------------------------------------------------------------------ harfler
def G_():
    a = math.radians(-35)
    return {'w': 2*R, 'd': [f"M {p(R+R*math.cos(a))} {p(50+R*math.sin(a))} "
                            f"A {p(R)} {p(R)} 0 1 0 {p(2*R)} 50 H {p(R-2)}"]}
def L_(): return {'w': L_W, 'd': [f"M 0 0 V {p(CAP)} H {p(L_W)}"]}
def O_(): return {'w': 2*R, 'd': [f"M 0 50 A {p(R)} {p(R)} 0 1 1 {p(2*R)} 50 "
                                  f"A {p(R)} {p(R)} 0 1 1 0 50 Z"]}
def B_():
    return {'w': B_STEM+B_BOWL, 'd': [
        f"M 0 0 V {p(CAP)}",
        f"M 0 0 H {p(B_STEM)} A {p(B_BOWL)} {p(B_BOWL)} 0 0 1 {p(B_STEM)} 50 H 0",
        f"M 0 50 H {p(B_STEM)} A {p(B_BOWL)} {p(B_BOWL)} 0 0 1 {p(B_STEM)} {p(CAP)} H 0"]}
def A_(bar=True):
    d = [f"M 0 {p(CAP)} L {p(A_W/2)} 0 L {p(A_W)} {p(CAP)}"]
    if bar:
        y = 70.0
        lx, rx = (A_W/2)*(1-y/CAP), (A_W/2)+(A_W/2)*(y/CAP)
        d.append(f"M {p(lx)} {p(y)} H {p(rx)}")
    return {'w': A_W, 'd': d}


KERN = {('G','L'): -3, ('L','O'): -15, ('O','B'): -7, ('B','A'): 3, ('A','L'): -5}
KERN_BAR = {('G','L'): -3, ('L','O'): -15, ('O','B'): -7, ('B','A'): 6, ('A','L'): 2}


def word(w, track, ink=INK, bar=False, cap='square'):
    seq = [('G',G_()),('L',L_()),('O',O_()),('B',B_()),('A',A_(bar)),('L',L_())]
    kern = KERN_BAR if bar else KERN
    parts, x = [], 0.0
    for i,(n,gl) in enumerate(seq):
        body = ''.join(f'<path d="{d}"/>' for d in gl['d'])
        parts.append(f'<g transform="translate({p(x)},0)">{body}</g>')
        x += gl['w'] + track
        if i+1 < len(seq):
            k = kern.get((n, seq[i+1][0]), 0)
            if k < 0: k += max(0.0, (w - 13.0) * 0.55)   # kalın ağırlık düzeltmesi
            x += k
    return (f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="{cap}" '
            f'stroke-linejoin="miter" stroke-miterlimit="10">{"".join(parts)}</g>'), x-track


def roofline(total, w, ink=INK):
    """Kelimenin üstünden geçen saçak. Tepe noktası A'nın apeksinde."""
    apex_x = total - (L_W + 28.0 + 2) - A_W/2 + A_W/2   # A'nın orta ekseni
    apex_x = total - L_W - 28.0 - A_W/2
    top, eave, over = -62.0, -30.0, 16.0
    return (f'<path d="M {p(-over)} {p(eave)} L {p(apex_x)} {p(top)} '
            f'L {p(total+over)} {p(eave)}" fill="none" stroke="{ink}" '
            f'stroke-width="{p(w)}" stroke-linecap="square" stroke-linejoin="miter"/>')


def svg(inner, x, y, w, h, extra=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{p(x)} {p(y)} {p(w)} {p(h)}" '
            f'width="{p(w)}" height="{p(h)}"{extra}>{inner}</svg>')


# ------------------------------------------------------------------ yönler
def y1_logo(ink=INK):
    """MİMARİ — ağır, sıkı, kesme uçlu."""
    m, tw = word(22.0, 30.0, ink)
    return svg(f'<g transform="translate(12,12)">{m}</g>', 0, 0, tw+24, CAP+24)

def y1_amblem(ink=INK):
    """Kare modül içinde çatı — yapı ve modülerlik."""
    w, S = 20.0, 116.0
    d = (f'<path d="M {p(S*0.14)} {p(S*0.60)} L {p(S/2)} {p(S*0.26)} L {p(S*0.86)} {p(S*0.60)}"/>'
         f'<path d="M {p(S*0.14)} {p(S*0.60)} V {p(S*0.84)} H {p(S*0.86)} V {p(S*0.60)}"/>')
    return svg(f'<rect x="{p(w/2)}" y="{p(w/2)}" width="{p(S-w)}" height="{p(S-w)}" '
               f'fill="none" stroke="{ink}" stroke-width="{p(w*0.55)}"/>'
               f'<g fill="none" stroke="{ink}" stroke-width="{p(w*0.85)}" '
               f'stroke-linecap="square" stroke-linejoin="miter">{d}</g>', 0, 0, S, S)


def y2_logo(ink=INK):
    """ÇATI ÇİZGİSİ — yapı bütün kelimeyi örter."""
    w = 10.0
    m, tw = word(w, 36.0, ink)
    return svg(f'<g transform="translate(18,80)">{roofline(tw, w, ink)}{m}</g>',
               0, 0, tw+36, CAP+96)

def y2_amblem(ink=INK):
    """Saçak tek başına — en indirgenmiş hâli."""
    w, W = 11.0, 108.0
    return svg(f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="square">'
               f'<path d="M 0 46 L {p(W/2)} 6 L {p(W)} 46"/>'
               f'<path d="M {p(W*0.22)} 74 H {p(W*0.78)}"/></g>', -8, -8, W+16, 96)


def y3_logo(ink=INK):
    """G MONOGRAM — wordmark sakin, imzayı amblem taşır. A klasik."""
    m, tw = word(13.0, 30.0, ink, bar=True)
    return svg(f'<g transform="translate(8,8)">{m}</g>', 0, 0, tw+16, CAP+16)

def y3_amblem(ink=INK):
    """Kare içinde G; G'nin üst omzu çatı açısıyla kesilir."""
    w, S = 17.0, 118.0
    c, r = S/2, S*0.30
    a1, a2 = math.radians(-52), math.radians(0)
    x1, y1 = c + r*math.cos(a1), c + r*math.sin(a1)
    g = (f'<path d="M {p(x1)} {p(y1)} A {p(r)} {p(r)} 0 1 0 {p(c+r)} {p(c)} H {p(c)}"/>'
         f'<path d="M {p(c - r*1.02)} {p(c - r*0.62)} L {p(c)} {p(c - r*1.30)} '
         f'L {p(c + r*1.02)} {p(c - r*0.62)}"/>')
    return svg(f'<rect x="{p(w/2)}" y="{p(w/2)}" width="{p(S-w)}" height="{p(S-w)}" '
               f'fill="none" stroke="{ink}" stroke-width="{p(w*0.5)}"/>'
               f'<g fill="none" stroke="{ink}" stroke-width="{p(w*0.85)}" '
               f'stroke-linecap="square" stroke-linejoin="miter">{g}</g>', 0, 0, S, S)


YONLER = {
    'y1-mimari':  (y1_logo, y1_amblem, 'MİMARİ', 'Ağır kesme uçlu harfler; kare modül amblemi'),
    'y2-catisi':  (y2_logo, y2_amblem, 'ÇATI ÇİZGİSİ', 'Saçak bütün kelimeyi örter; A tepede'),
    'y3-monogram':(y3_logo, y3_amblem, 'G MONOGRAM', 'Wordmark sakin, imzayı kare içindeki G taşır'),
}

if __name__ == '__main__':
    n = 0
    for key, (lg, am, _, _) in YONLER.items():
        for tag, ink in (('siyah', INK), ('beyaz', '#FFFFFF')):
            open(os.path.join(OUT, f'{key}-logo-{tag}.svg'), 'w').write(lg(ink)); n += 1
            open(os.path.join(OUT, f'{key}-amblem-{tag}.svg'), 'w').write(am(ink)); n += 1
    print(f'{n} SVG → {OUT}')
