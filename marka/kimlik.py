#!/usr/bin/env python3
"""
GLOBAL YAPI GELİŞTİRME A.Ş. — v5, baştan farklı yaklaşım.

Önceki denemelerden farkı:
  · A artık çatı değil — normal harf. Çatı fikri simgeye taşındı.
  · Harfler elle çizilmiyor, hazır yazı tipleriyle deneniyor.
  · Simge çizgisel değil DOLU düzlemlerden kuruluyor (Gmail mantığı).
  · Kilit dikey: GLOBAL üstte, YAPI GELİŞTİRME A.Ş. altında.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
INK, PAPER, TAN, DEEP = '#1A1A18', '#FBFAF7', '#C3B4A0', '#3E3E3A'

# Aday yazı tipleri — hepsi SIL OFL, ticari kullanıma açık.
FONTLAR = [
    ('Jost',             500, .30, 'Geometrik · Futura ruhu, zarif ama sağlam'),
    ('Archivo',          600, .22, 'Grotesk · kurumsal, dayanıklı'),
    ('Space Grotesk',    500, .24, 'Karakterli · teknik ve çağdaş'),
    ('Barlow Condensed', 600, .26, 'Kondens · endüstriyel, tabela dili'),
    ('Bebas Neue',       400, .28, 'Kapitals · güçlü, doğrudan'),
    ('Montserrat',       600, .22, 'Geometrik · güvenli, yaygın'),
]


def simge(kind, a=INK, b=TAN, r=22):
    """Dolu düzlemlerden kurulu simgeler. Hepsi 100×100."""
    if kind == 'kart':
        # Yuvarlatılmış kart + içinde katlanmış çatı — Gmail'e en yakın kurgu.
        return (f'<rect width="100" height="100" rx="{r}" fill="{a}"/>'
                f'<path d="M50 24 L86 58 L86 76 L50 42 Z" fill="{b}"/>'
                f'<path d="M50 24 L14 58 L14 76 L50 42 Z" fill="{PAPER}"/>')
    if kind == 'katman':
        # Çerçevesiz iki düzlem: ışık alan ve gölgede kalan çatı yüzeyi.
        return (f'<path d="M50 10 L94 52 L94 78 L50 36 Z" fill="{a}"/>'
                f'<path d="M50 10 L6 52 L6 78 L50 36 Z" fill="{b}"/>')
    if kind == 'blok':
        # Çatı + gövde, iki ton, tek kütle.
        return (f'<path d="M50 12 L94 50 L6 50 Z" fill="{a}"/>'
                f'<rect x="20" y="50" width="60" height="38" rx="3" fill="{b}"/>')
    if kind == 'modul':
        # Üst üste iki modül + çatı — modüler yapı.
        return (f'<path d="M50 8 L92 44 L8 44 Z" fill="{a}"/>'
                f'<rect x="16" y="50" width="68" height="18" rx="3" fill="{b}"/>'
                f'<rect x="16" y="72" width="68" height="18" rx="3" fill="{DEEP}"/>')
    if kind == 'kesit':
        # Negatif alanda çatı: dolu karenin içinden Λ oyulmuş.
        return (f'<path d="M0 0 H100 V100 H0 Z M50 30 L84 64 V84 H16 V64 Z" '
                f'fill="{a}" fill-rule="evenodd"/>')
    # 'catikart' — kart içinde tek parça dolu çatı
    return (f'<rect width="100" height="100" rx="{r}" fill="{b}"/>'
            f'<path d="M50 26 L84 58 H70 V78 H30 V58 H16 Z" fill="{a}"/>')


SIMGELER = [
    ('kart',     'Kart · katlanmış çatı', 'Gmail kurgusuna en yakın: kart + iki düzlem'),
    ('katman',   'Katman · çerçevesiz',   'İki yüzey, ışık ve gölge; çerçeve yok'),
    ('blok',     'Blok · çatı + gövde',   'Tek kütle, iki ton'),
    ('modul',    'Modül · üst üste',      'Modüler yapıyı doğrudan anlatır'),
    ('kesit',    'Kesit · negatif alan',  'Çatı oyularak elde edilir'),
    ('catikart', 'Kart · dolu ev',        'Açık kart üzerine koyu ev silueti'),
]


def svg(inner, s=100):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" '
            f'width="{s}" height="{s}">{inner}</svg>')


def kilit(font, weight, track, ink=INK, sim='kart', boy=64):
    """Dikey kilit: simge üstte, GLOBAL, altında açıklama."""
    return f'''<div style="text-align:center">
      <div style="margin-bottom:16px">{svg(simge(sim), boy)}</div>
      <div style="font-family:'{font}',sans-serif;font-weight:{weight};font-size:40px;
                  letter-spacing:{track}em;color:{ink};line-height:1;
                  text-indent:{track}em">GLOBAL</div>
      <div style="font-family:'{font}',sans-serif;font-weight:400;font-size:10px;
                  letter-spacing:.34em;color:{ink};opacity:.72;margin-top:9px;
                  text-indent:.34em">YAPI GELİŞTİRME A.Ş.</div>
    </div>'''


if __name__ == '__main__':
    for k, _, _ in SIMGELER:
        open(os.path.join(OUT, 'svg-v5', f'simge-{k}.svg'), 'w').write(svg(simge(k)))
    print('ok')
