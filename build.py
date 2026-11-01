"""Génère une copie de index.html par page de soin (lahochi.html, ...).

GitHub Pages sert lahochi.html à l'adresse namazen59.fr/lahochi.
À relancer après chaque modification de index.html : python3 build.py
"""
import html, re

src = open('index.html', encoding='utf-8').read()
for slug, title in re.findall(r'id="p-([a-z-]+)" data-title="([^"]+)"', src):
    url = f'https://namazen59.fr/{slug}'
    out = src.replace('<link rel="canonical" href="https://namazen59.fr/">', f'<link rel="canonical" href="{url}">')
    out = out.replace('<meta property="og:url" content="https://namazen59.fr/">', f'<meta property="og:url" content="{url}">')
    out = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', out, count=1)
    out = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', out, count=1)
    # la page s'affiche directement, sans attendre le script
    out = out.replace('<div id="home">', '<div id="home" hidden>', 1)
    out = out.replace(f'id="p-{slug}" data-title="{title}" hidden>', f'id="p-{slug}" data-title="{title}">', 1)
    open(f'{slug}.html', 'w', encoding='utf-8').write(out)
    print(f'{slug}.html')
