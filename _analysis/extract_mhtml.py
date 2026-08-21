import sys, os, re, base64

def extract(src, outdir):
    with open(src, 'rb') as f:
        data = f.read()
    # find boundary
    m = re.search(rb'boundary="([^"]+)"', data[:2000])
    if not m:
        print("no boundary in", src); return
    boundary = m.group(1)
    parts = data.split(b'--' + boundary)
    for i, part in enumerate(parts[1:], 1):
        if part.strip() in (b'', b'--'):
            continue
        header, _, body = part.partition(b'\r\n\r\n')
        if not body:
            header, _, body = part.partition(b'\n\n')
        htxt = header.decode('latin1')
        loc = re.search(r'Content-Location:\s*(\S+)', htxt)
        ctype = re.search(r'Content-Type:\s*([^;\r\n]+)', htxt)
        enc = re.search(r'Content-Transfer-Encoding:\s*(\S+)', htxt)
        locname = loc.group(1) if loc else None
        ct = ctype.group(1).strip() if ctype else ''
        if enc and enc.group(1).lower() == 'base64':
            body = base64.b64decode(re.sub(rb'\s', b'', body))
        if 'text/html' in ct or 'css' in ct or 'javascript' in ct or 'json' in ct:
            try:
                txt = body.decode('utf-8')
            except Exception:
                txt = body.decode('latin1')
            name = f"{i:03d}_{'html' if 'html' in ct else ('css' if 'css' in ct else ('js' if 'javascript' in ct else 'txt'))}"
            if locname:
                name = f"{i:03d}_{os.path.basename(locname).split('?')[0] or 'file'}"
                if not re.search(r'\.(html|css|js|txt|json)$', name): name += f".{name.split('_')[-1] if False else 'txt'}"
            with open(os.path.join(outdir, name), 'w') as g:
                g.write(txt)
        else:
            if locname:
                base = os.path.basename(locname).split('?')[0]
                if not base: base = f"part{i}"
            else:
                base = f"part{i}"
            with open(os.path.join(outdir, base), 'wb') as g:
                g.write(body)
    print(src, "->", len(os.listdir(outdir)), "parts")

extract('/home/user/Testong/ROBLOX - ROBLOX', '/home/user/Testong/_analysis/mhtml1')
extract('/home/user/Testong/Style Guide', '/home/user/Testong/_analysis/mhtml2')
extract('/home/user/Testong/TheKentuckian - ROBLOX', '/home/user/Testong/_analysis/mhtml3')
