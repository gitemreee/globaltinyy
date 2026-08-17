#!/usr/bin/env python3
"""
GLOBAL amblemi — mevcut logodan ölçülerek vektöre çevrildi.

Amblem "G" harfini bir ev kesitiyle birleştirir: sol duvar + taban G'nin
gövdesi, ortadaki yatay çubuk G'nin kirişi, bakır parçalar vurgu.

Çatı yüksekliği parametrik (`tepe`): 0 = orijinal, artırıldıkça çatı
aşağı doğru kısalır.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg-marka')
os.makedirs(OUT, exist_ok=True)

# Marka renkleri (kimlik dosyasından)
INK   = '#2F3336'   # ana renk · antrasit
BRONZ = '#B87333'   # bakır bronz · vurgu
GRI   = '#A6A39A'   # nötr gri
KAGIT = '#F5F3F0'

W = 810.0           # çizim genişliği (yükseklik 1000 referansında)
KAL = 75.0          # şerit kalınlığı
EGIM = 1.354        # çatı eğimi (dx/dy)


def _n(v): return f"{v:.1f}".rstrip('0').rstrip('.')


def amblem_svg(tepe=0.0, ink=INK, bronz=BRONZ, tek_renk=None):
    """tepe: çatı tepesinin y'si. Büyüdükçe çatı kısalır (aşağı iner)."""
    if tek_renk:
        ink = bronz = tek_renk

    apex_x = 405.0
    etek_dis = 299.0                   # çatının duvara indiği kot — sabit
    h = etek_dis - tepe                # çatı yüksekliği; tepe indikçe azalır
    # Şerit kalınlığı eğime dik ölçülür; dikey izdüşümü eğimle birlikte değişir.
    boy = (apex_x ** 2 + h ** 2) ** 0.5
    ic_tepe = tepe + KAL * boy / apex_x
    sol_ic_y = ic_tepe + (apex_x - KAL) * h / apex_x
    sag_kesim_y = ic_tepe + 269.0 * h / 299.0
    sag_kesim_x = apex_x + (apex_x / h) * (sag_kesim_y - ic_tepe)

    taban_ust, taban_alt = 910.0, 1000.0
    dikey_x0, dikey_x1, dikey_ust = 374.0, 451.0, 750.0

    # Ev kesiti + taban: tek kapalı şekil
    ev = (f"M 0 {_n(taban_alt)} L 0 {_n(etek_dis)} L {_n(apex_x)} {_n(tepe)} "
          f"L {_n(W)} {_n(etek_dis)} L {_n(sag_kesim_x)} {_n(sag_kesim_y)} "
          f"L {_n(apex_x)} {_n(ic_tepe)} L {_n(KAL)} {_n(sol_ic_y)} "
          f"L {_n(KAL)} {_n(taban_ust)} L {_n(dikey_x0)} {_n(taban_ust)} "
          f"L {_n(dikey_x0)} {_n(dikey_ust)} L {_n(dikey_x1)} {_n(dikey_ust)} "
          f"L {_n(dikey_x1)} {_n(taban_alt)} Z")

    # G kirişi — sağ ucu 45° kesik
    kiris = "M 247 585 L 560 585 L 640 675 L 247 675 Z"

    # Dörtlü pencere
    pen = ''.join(
        f'<rect x="{x}" y="{y}" width="48" height="56" fill="{ink}"/>'
        for x in (342, 420) for y in (300, 382))

    # Bakır: çatı ucundaki eğik parça + kirişten inen dikey
    egik = f"M {_n(W)} 348 L 645 500 L 645 600 L {_n(W)} 462 Z"
    dikey = "M 557 675 L 632 675 L 632 1000 L 557 1000 Z"

    yuk = 1000.0 - tepe
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 {_n(tepe)} {_n(W)} {_n(yuk)}" '
            f'width="{_n(W)}" height="{_n(yuk)}">'
            f'<path d="{ev}" fill="{ink}"/><path d="{kiris}" fill="{ink}"/>{pen}'
            f'<path d="{egik}" fill="{bronz}"/><path d="{dikey}" fill="{bronz}"/></svg>')


VARYANT = {
    'orijinal':  0.0,
    'kisa':      70.0,
    'daha-kisa': 130.0,
}

if __name__ == '__main__':
    n = 0
    for ad, t in VARYANT.items():
        for tag, kw in (('renkli', {}), ('antrasit', {'tek_renk': INK}),
                        ('beyaz', {'tek_renk': '#FFFFFF'})):
            open(os.path.join(OUT, f'amblem-{ad}-{tag}.svg'), 'w').write(
                amblem_svg(t, **kw)); n += 1
    print(f'{n} SVG → {OUT}')
