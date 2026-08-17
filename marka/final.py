#!/usr/bin/env python3
"""
GLOBAL YAPI GELİŞTİRME A.Ş. — seçilen yön: ÇATI ÇİZGİSİ, endüstriyel ton.

Fikir: çatı tek bir harfe sıkışmaz. Saçak bütün kelimenin üstünden geçer ve
A'nın tam apeksinde kırılır — yapı, markanın üstünü örter.

Ton: güçlü / endüstriyel. Kalın çizgi, kesme uçlar, sıkı dizgi.
"""
import os, math

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg-final')
os.makedirs(OUT, exist_ok=True)

CAP, R, L_W = 100.0, 44.0, 58.0
A_W, B_BOWL, B_STEM = 76.0, 25.0, 28.0
INK, PAPER, TAN, STEEL = '#1A1A18', '#FBFAF7', '#C3B4A0', '#6E6A64'


def p(v): return f"{v:.2f}".rstrip('0').rstrip('.')


# ------------------------------------------------------------------ harfler
def G_(bar=-2.0):
    """bar: G'nin iç çubuğunun bittiği x (merkeze göre; küçüldükçe uzar)."""
    a = math.radians(-35)
    return {'w': 2*R, 'd': [f"M {p(R+R*math.cos(a))} {p(50+R*math.sin(a))} "
                            f"A {p(R)} {p(R)} 0 1 0 {p(2*R)} 50 H {p(R+bar)}"]}
def L_(): return {'w': L_W, 'd': [f"M 0 0 V {p(CAP)} H {p(L_W)}"]}
def O_(): return {'w': 2*R, 'd': [f"M 0 50 A {p(R)} {p(R)} 0 1 1 {p(2*R)} 50 "
                                  f"A {p(R)} {p(R)} 0 1 1 0 50 Z"]}
def B_(): return {'w': B_STEM+B_BOWL, 'd': [
    f"M 0 0 V {p(CAP)}",
    f"M 0 0 H {p(B_STEM)} A {p(B_BOWL)} {p(B_BOWL)} 0 0 1 {p(B_STEM)} 50 H 0",
    f"M 0 50 H {p(B_STEM)} A {p(B_BOWL)} {p(B_BOWL)} 0 0 1 {p(B_STEM)} {p(CAP)} H 0"]}
def A_(): return {'w': A_W, 'd': [f"M 0 {p(CAP)} L {p(A_W/2)} 0 L {p(A_W)} {p(CAP)}"]}

KERN = {('G','L'): -3, ('L','O'): -15, ('O','B'): -7, ('B','A'): 3, ('A','L'): -5}


def word(w, track, ink=INK, gbar=-2.0):
    """GLOBAL. Döner: (svg, toplam_genişlik, {harf_indeksi: x_konumu})."""
    seq = [('G',G_(gbar)),('L',L_()),('O',O_()),('B',B_()),('A',A_()),('L',L_())]
    parts, pos, x = [], {}, 0.0
    for i,(n,gl) in enumerate(seq):
        pos[i] = x
        parts.append(f'<g transform="translate({p(x)},0)">'
                     + ''.join(f'<path d="{d}"/>' for d in gl['d']) + '</g>')
        x += gl['w'] + track
        if i+1 < len(seq):
            k = KERN.get((n, seq[i+1][0]), 0)
            if k < 0: k += max(0.0, (w - 13.0) * 0.55)   # kalın ağırlıkta optik düzeltme
            x += k
    g = (f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="butt" '
         f'stroke-linejoin="miter" stroke-miterlimit="10">{"".join(parts)}</g>')
    return g, x - track, pos


def roof(total, apex_x, w, ink=INK, ayak=16.0, top=-76.0, eave=-32.0, over=20.0):
    """Saçak. A'nın apeksinde kırılır; uçlarda mertek ayakları aşağı iner."""
    d = f"M {p(-over)} {p(eave)} L {p(apex_x)} {p(top)} L {p(total+over)} {p(eave)}"
    out = f'<path d="{d}"/>'
    if ayak:
        # Mertek ucu: çatıyı kelimeye kilitleyen kısa dikey iniş.
        out += (f'<path d="M {p(-over)} {p(eave)} V {p(eave+ayak)}"/>'
                f'<path d="M {p(total+over)} {p(eave)} V {p(eave+ayak)}"/>')
    return (f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="butt" '
            f'stroke-linejoin="miter" stroke-miterlimit="10">{out}</g>')


def svg(inner, x, y, w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{p(x)} {p(y)} {p(w)} {p(h)}" '
            f'width="{p(w)}" height="{p(h)}">{inner}</svg>')


# ------------------------------------------------------------------ kilitler
W, TRACK = 17.0, 26.0          # endüstriyel ağırlık


def logo(ink=INK, ayak=16.0, desc=True, w=W, track=TRACK,
         top=-76.0, eave=-32.0, over=20.0, roof_r=0.72, gbar=-2.0):
    m, tw, pos = word(w, track, ink, gbar)
    apex = pos[4] + A_W/2                       # A'nın tam orta ekseni
    body = roof(tw, apex, w * roof_r, ink, ayak, top, eave, over) + m
    top = top - w/2 - 6
    h = CAP - top + (34 if desc else 0) + 8
    if desc:
        body += (f'<text x="0" y="{p(CAP + 30)}" '
                 f'font-family="Liberation Sans, Arial, sans-serif" font-size="15" '
                 f'font-weight="700" letter-spacing="5.6" fill="{ink}">YAPI GELİŞTİRME A.Ş.</text>')
    return svg(f'<g transform="translate({p(20+w/2)},{p(-top)})">{body}</g>',
               0, 0, tw + 40 + w, h)


def amblem(kind='portal', ink=INK, w=17.0):
    """portal = çatı + iki ayak · sacak = çatı + alt çizgi · kare = çerçeve içinde çatı"""
    Wd = 112.0
    if kind == 'portal':
        d = (f'<path d="M 0 44 L {p(Wd/2)} 4 L {p(Wd)} 44"/>'
             f'<path d="M 0 44 V 96"/><path d="M {p(Wd)} 44 V 96"/>')
        return svg(f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="butt" '
                   f'stroke-linejoin="miter" stroke-miterlimit="10">{d}</g>',
                   -w/2-4, -4, Wd+w+8, 108)
    if kind == 'sacak':
        d = (f'<path d="M 0 46 L {p(Wd/2)} 6 L {p(Wd)} 46"/>'
             f'<path d="M {p(Wd*0.20)} 80 H {p(Wd*0.80)}"/>')
        return svg(f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="butt">{d}</g>',
                   -w/2-4, -4, Wd+w+8, 96)
    S = 116.0
    d = f'<path d="M {p(S*0.18)} {p(S*0.62)} L {p(S/2)} {p(S*0.30)} L {p(S*0.82)} {p(S*0.62)}"/>'
    return svg(f'<rect x="{p(w/2)}" y="{p(w/2)}" width="{p(S-w)}" height="{p(S-w)}" '
               f'fill="none" stroke="{ink}" stroke-width="{p(w*0.6)}"/>'
               f'<g fill="none" stroke="{ink}" stroke-width="{p(w)}" stroke-linecap="butt" '
               f'stroke-linejoin="miter">{d}</g>', 0, 0, S, S)


if __name__ == '__main__':
    n = 0
    for tag, ink in (('siyah', INK), ('beyaz', '#FFFFFF'), ('greige', TAN)):
        open(os.path.join(OUT, f'logo-yatay-{tag}.svg'), 'w').write(logo(ink)); n += 1
        open(os.path.join(OUT, f'wordmark-{tag}.svg'), 'w').write(logo(ink, desc=False)); n += 1
        for k in ('portal', 'sacak', 'kare'):
            open(os.path.join(OUT, f'amblem-{k}-{tag}.svg'), 'w').write(amblem(k, ink)); n += 1
    print(f'{n} SVG → {OUT}')
