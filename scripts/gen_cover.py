#!/usr/bin/env python3
"""
Generate the social/share cover for the 500k-downloads post (1200x630 OG ratio,
navy background with safe padding): Sniffnet bird mark on top, the bold headline
"500k downloads" in a gradient matching the donut palette, and the two
legend-less donuts below.

Emits the SVG to stdout (no cover.svg on disk). Run from repo root (AFTER the
donut data in gen_download_charts.py is current):
    python3 scripts/gen_cover.py | rsvg-convert -w 1200 \
        -o assets/img/post/500k-downloads/cover.png

Reuses donut drawing + segment data from scripts/gen_download_charts.py and the
bird glyph from favicon.svg (background square stripped). Palette order (donuts
clockwise from top AND caption gradient left->right): cyan->pink->purple->orange.
"""

import math, re
src=open("scripts/gen_download_charts.py").read().split('_all=os_seg')[0]
g={}; exec(src,g)
pol,arc,logo_at=g["pol"],g["arc"],g["logo_at"]
os_seg,src_seg=g["os_seg"],g["src_seg"]
RING_LOGO="#0f1e3c"

def sniffnet_icon(cx_center,top,size):
    """Bird glyph from favicon.svg (background square removed), scaled/placed."""
    t=open("favicon.svg").read()
    inner=t[t.index('>',t.index('<svg'))+1 : t.rindex('</svg>')]
    inner=re.sub(r'<rect[^>]*id="rect24"[^>]*/>','',inner)   # drop bg square
    s=size/1024.0; gx=cx_center-size/2
    tx=gx-50*s; ty=top-146.397*s
    return f'<g transform="translate({tx:.3f},{ty:.3f}) scale({s:.5f})">{inner}</g>'

def donut(cx,cy,Rout,T,RMK,segs):
    RC=Rout-T/2; RIN=Rout-T; total=sum(s[1] for s in segs); out=[]; a=0.0
    for name,val,disp,color,logo in segs:
        sweep=val/total*360; a1=a+sweep; mid=(a+a1)/2
        out.append(f'<path d="{arc(cx,cy,RC,a,a1+0.4)}" fill="none" stroke="{color}" stroke-width="{T}"/>')
        if RC*math.radians(sweep) >= RMK+2:    # logo fits in segment (only tiny Docker falls to the hole)
            px,py=pol(cx,cy,RC,mid); out.append(logo_at(logo,RING_LOGO,px,py,RMK))
        else:
            x0,y0=pol(cx,cy,RIN,mid); x1,y1=pol(cx,cy,RIN-13,mid); lx,ly=pol(cx,cy,RIN-13-RMK/2,mid)
            out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>')
            out.append(logo_at(logo,color,lx,ly,RMK))
        a=a1
    return "\n".join(out)

W,H=1200,630
p=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" font-family="\'Helvetica Neue\', Arial, sans-serif">']
p.append(f'<rect width="{W}" height="{H}" fill="#0f1e3c"/>')
p.append('<defs><linearGradient id="grad" x1="0" y1="0" x2="1" y2="0">'
         '<stop offset="0" stop-color="#38cdde"/><stop offset="0.333" stop-color="#f57ec0"/>'
         '<stop offset="0.667" stop-color="#a06ee8"/><stop offset="1" stop-color="#f59a4d"/>'
         '</linearGradient></defs>')
p.append(sniffnet_icon(W/2, 44, 150))                      # brand mark, top-center (visible bird ~= caption height)
p.append(f'<text x="{W/2}" y="300" fill="url(#grad)" font-size="104" font-weight="800" text-anchor="middle">500k downloads</text>')
p.append(donut(442,478,106,40,30,os_seg))                  # two legend-less donuts, generous side margins
p.append(donut(758,478,106,40,30,src_seg))
p.append('</svg>')
import sys
sys.stdout.write("\n".join(p)+"\n")                        # emit SVG to stdout; pipe into rsvg-convert (no cover.svg on disk)
