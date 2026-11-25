"""Build index.html from src/index.src.html: gallery + hand-drawn floral motifs.
Usage: python3 tools/build.py            -> index.html
       python3 tools/build.py --preview OUT.html  -> standalone file with embedded assets
"""
import json, math, re, sys, base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
G = json.loads((ROOT / 'tools' / 'gallery.json').read_text())

# ---------- line-art motifs (viewBox, [(class, path)]) ----------
def circle(cx, cy, r):
    return f"M{cx+r} {cy} a{r} {r} 0 1 0 {-2*r} 0 a{r} {r} 0 1 0 {2*r} 0"

def gerbera():
    ps = [('b', circle(100, 100, 13)), ('b', circle(100, 100, 6))]
    for k in range(16):
        a = k / 16 * 2 * math.pi
        x1, y1 = 100 + 18 * math.cos(a), 100 + 18 * math.sin(a)
        x2, y2 = 100 + 70 * math.cos(a), 100 + 70 * math.sin(a)
        ox, oy = -math.sin(a) * 7, math.cos(a) * 7
        ps.append(('a' if k % 2 else 'b', f"M{x1:.1f} {y1:.1f} Q{(x1+x2)/2+ox:.1f} {(y1+y2)/2+oy:.1f} {x2:.1f} {y2:.1f} Q{(x1+x2)/2-ox:.1f} {(y1+y2)/2-oy:.1f} {x1:.1f} {y1:.1f}"))
    ps.append(('a', "M100 172 C100 190 98 210 94 238"))
    ps.append(('a', "M98 212 C120 198 140 200 152 214 C130 222 112 222 98 212"))
    return ('0 0 200 240', ps)

def eucalyptus():
    ps = [('a', "M80 258 C84 200 70 150 86 90 C96 50 84 24 92 4")]
    for cx, cy, r in [(60,225,13),(104,200,12),(58,170,12),(104,140,11),(66,112,10),(104,82,10),(72,56,9),(102,30,8)]:
        ps.append(('a', circle(cx, cy, r)))
    return ('0 0 160 260', ps)

MOTIFS = {
 'strelitzia': ('0 0 230 270', [
   ('a', "M110 266 C108 220 104 180 98 140"),
   ('i', "M98 140 C130 128 170 120 214 112 C176 134 136 146 98 146"),
   ('b', "M128 128 C130 96 140 66 160 30 C152 70 146 100 140 126"),
   ('b', "M144 124 C156 98 176 76 204 58 C182 84 168 104 156 122"),
   ('b', "M120 130 C116 104 118 78 128 52 C128 82 128 104 128 128"),
   ('i', "M150 120 C170 108 188 100 206 96"),
   ('a', "M104 236 C70 218 46 182 44 134 C72 156 94 192 104 236"),
   ('a', "M104 236 C84 206 62 172 44 134"),
   ('a', "M112 214 C140 200 168 174 184 144 C154 156 128 180 112 214"),
 ]),
 'leaf': ('0 0 160 260', [
   ('a', "M80 255 C30 200 18 120 70 10 C130 90 138 190 80 255"),
   ('a', "M80 255 C76 180 74 100 70 10"),
   ('a', "M77 200 C60 185 46 170 38 150"), ('a', "M77 200 C96 186 112 170 120 152"),
   ('a', "M75 150 C58 132 46 116 40 96"), ('a', "M75 150 C94 134 108 116 116 98"),
   ('a', "M73 100 C60 86 52 72 50 58"), ('a', "M73 100 C86 86 96 72 100 58"),
 ]),
 'rose': ('0 0 200 210', [
   ('b', "M100 100 C110 92 120 104 110 114 C96 128 78 110 86 94 C96 74 128 80 132 104 C136 132 104 148 82 138 C56 126 56 92 74 74 C96 52 140 60 150 96"),
   ('i', "M150 96 C156 130 132 160 100 162 C64 164 42 136 46 104"),
   ('i', "M46 104 C48 70 74 46 106 46 C134 46 154 64 156 84"),
   ('a', "M100 162 C100 180 96 196 92 208"),
   ('a', "M98 184 C120 172 140 174 150 186 C128 194 112 192 98 184"),
 ]),
 'vine': ('0 0 640 80', [
   ('i', "M4 50 C80 20 120 70 200 44 S320 14 380 44 S520 74 636 36"),
   ('a', "M196 44 c6-16 26-20 34-10 c-12 2-22 6-34 10"),
   ('a', "M380 44 c-6 14-24 18-34 12 c12-2 22-6 34-12"),
   ('a', "M520 56 c6-16 26-18 34-8 c-12 2-22 4-34 8"),
   ('a', "M90 38 c-4-14 6-28 20-28 c-4 10-10 20-20 28"),
   ('b', "M292 24 a5 5 0 1 0 -10 0 a5 5 0 1 0 10 0"),
   ('b', "M458 62 a5 5 0 1 0 -10 0 a5 5 0 1 0 10 0"),
   ('i', "M380 44 C392 30 410 28 418 36 C424 44 414 52 406 46"),
 ]),
 'gerbera': gerbera(),
 'eucalyptus': eucalyptus(),
}

def motif(name, style, speed=0.1, flip=False):
    vb, ps = MOTIFS[name]
    tr = ' transform="scale(-1,1)"' if flip else ''
    w = vb.split()[2]
    g = ''.join(f'<path class="{c}" d="{d}" pathLength="1"/>' for c, d in ps)
    inner = f'<g transform="translate({w},0) scale(-1,1)">{g}</g>' if flip else g
    return f'<svg class="g" data-speed="{speed}" viewBox="{vb}" style="{style}" aria-hidden="true">{inner}</svg>'

PLACE = {
 'hero': [motif('strelitzia', 'left:2vw;top:16vh;width:clamp(120px,15vw,240px)', 0),
          motif('eucalyptus', 'right:3vw;top:20vh;width:clamp(80px,8vw,130px)', 0, True),
          motif('vine', 'left:-4vw;bottom:3vh;width:clamp(260px,34vw,560px)', 0)],
 'occ': [motif('leaf', 'right:-2vw;top:8%;width:clamp(120px,14vw,220px)', .12, True),
         motif('gerbera', 'left:38%;top:4%;width:clamp(90px,9vw,150px)', .08),
         motif('vine', 'left:-3vw;bottom:6%;width:clamp(280px,40vw,620px)', .05)],
 'kiosk': [motif('strelitzia', 'right:2vw;top:6%;width:clamp(140px,16vw,260px)', .14, True),
           motif('eucalyptus', 'left:1vw;bottom:10%;width:clamp(80px,8vw,130px)', .1)],
 'studio': [motif('rose', 'left:46%;top:6%;width:clamp(110px,11vw,180px)', .1),
            motif('leaf', 'left:-3vw;bottom:-4%;width:clamp(110px,12vw,190px)', .14)],
 'reviews': [motif('gerbera', 'right:4vw;top:6%;width:clamp(110px,11vw,180px)', .1),
             motif('eucalyptus', 'left:2vw;top:44%;width:clamp(70px,7vw,110px)', .08, True)],
 'contact': [motif('vine', 'right:-6vw;top:10%;width:clamp(280px,36vw,560px)', .06, True),
             motif('rose', 'left:44%;bottom:6%;width:clamp(100px,10vw,160px)', .1)],
 'foot': [motif('strelitzia', 'right:3vw;bottom:-10px;width:clamp(140px,14vw,220px)', 0, True)],
}

SIZES = ['s1', 's2', 's3', 's1', 's3', 's2']

def gallery():
    out = []
    for k, it in enumerate(G):
        i, w, h = it['id'], it['w'], it['h']
        out.append(
            f'<figure class="gi {SIZES[k % len(SIZES)]}" data-cat="{it["cat"]}" tabindex="0" role="button" aria-label="Powiększ: {it["alt"]}">'
            f'<img src="img/g/{i}-640.webp" srcset="img/g/{i}-640.webp 640w, img/g/{i}-1280.webp 1280w" sizes="(max-width:860px) 80vw, 40vw" '
            f'width="{w}" height="{h}" loading="lazy" decoding="async" alt="{it["alt"]}" data-full="img/g/{i}-1280.webp">'
            f'<figcaption>{it["alt"]}</figcaption></figure>')
    return '\n'.join(out)

src = (ROOT / 'src' / 'index.src.html').read_text()
src = src.replace('<!--SYMBOLS-->', '')
src = src.replace('<!--GALLERY-->', gallery())
for k, v in PLACE.items():
    src = src.replace(f'<!--G:{k}-->', '\n'.join(v))
assert '<!--G:' not in src

if len(sys.argv) > 2 and sys.argv[1] == '--preview':
    def d(p):
        f = ROOT / p
        mt = {'webp': 'image/webp', 'png': 'image/png', 'woff2': 'font/woff2'}[f.suffix[1:]]
        return f'data:{mt};base64,' + base64.b64encode(f.read_bytes()).decode()
    src = re.sub(r'data-full="img/g/(\d+)-1280.webp"', r'data-full="img/g/\1-640.webp"', src)
    s = re.sub(r'url\(((?:fonts|img)/[^)]+)\)', lambda m: f'url({d(m.group(1))})', src)
    s = re.sub(r' srcset="[^"]*"', '', s)
    s = re.sub(r'(src|href|data-full|data-img)="((?:img|fonts)/[^"]+)"', lambda m: f'{m.group(1)}="{d(m.group(2))}"', s)
    s = s.replace('rel="preload"', 'rel="x"')
    pathlib.Path(sys.argv[2]).write_text(s)
    print('preview', len(s) // 1024, 'KB')
else:
    (ROOT / 'index.html').write_text(src)
    print('index.html', len(src) // 1024, 'KB')
