import numpy as np
from PIL import Image, ImageDraw

orig = np.array(Image.open('/home/user/Testong/B0CSUKJCMAAVIq9.webp').convert('RGB')).astype(int)

# ---- paint recreation (non-text elements only) ----
canvas = Image.new('RGB', (680, 510), (255, 255, 255))
d = ImageDraw.Draw(canvas)

def draw_rect(x0, y0, x1, y1, color, radius=0):
    d.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=color)

def draw_ellipse(cx, cy, rx, ry, fill, outline=None, rot=0):
    bbox = [cx - rx, cy - ry, cx + rx, cy + ry]
    if outline:
        d.ellipse(bbox, fill=fill, outline=outline, width=1)
    else:
        d.ellipse(bbox, fill=fill)

# menu icon
for (sx, sy) in [(13, 8), (18, 8), (23, 8), (13, 13), (18, 13), (23, 13), (13, 17), (18, 17), (23, 17)]:
    draw_rect(sx, sy, sx + 4, sy + 4, (10, 22, 56), 1)
# logo (mask rects)
for (x, y, w) in [(6,3,1),(8,4,3),(6,5,6),(5,6,6),(2,7,9),(2,8,9),(2,9,9),(5,10,6),(7,11,5),(9,12,2)]:
    draw_rect(31 + x, 6 + y, 31 + x + w, 7 + y, (173, 173, 173))
# pill
draw_rect(277, 29, 334, 34, (211, 211, 211), 2)
# hairline
d.rectangle([373, 33, 660, 33], fill=(224, 224, 224))
# robux
draw_ellipse(537.5, 14, 8, 5, (200, 240, 191), (108, 185, 111))
# tickets
draw_rect(597, 8, 608, 20, (232, 217, 174), 3)
draw_rect(603, 10, 606, 18, (217, 142, 85))
# palette
for (cx, cy) in [(141.5, 425.5), (94, 459.5), (125.5, 459.5), (157, 459.5), (188.5, 459.5),
                 (94, 485.5), (125.5, 485.5), (157, 485.5), (188.5, 485.5),
                 (124.5, 517.5), (156.5, 517.5)]:
    draw_ellipse(cx, cy, 15.5, 15.5, (255, 204, 153))
d.rectangle([0, 404, 100, 510], fill=(255, 255, 255))  # left clip
# create new outfit button
d.rounded_rectangle([583, 57, 655, 75], radius=9, fill=(255, 255, 255), outline=(229, 229, 229), width=1)
# page chips
d.rounded_rectangle([424, 339, 444, 356], radius=8, fill=(252, 252, 252), outline=(232, 232, 232), width=1)
d.rounded_rectangle([500, 339, 520, 356], radius=8, fill=(255, 255, 255), outline=(176, 176, 176), width=1)
# dividers
d.rectangle([260, 374, 639, 374], fill=(229, 229, 229))
d.rectangle([261, 375, 638, 375], fill=(241, 241, 241))
# remove buttons
for bx in [322, 413, 504, 595]:
    d.rounded_rectangle([bx, 425, bx + 35, 442], radius=4, fill=(64, 132, 219))
# online chip
d.rounded_rectangle([623, 492, 676, 509], radius=8, fill=(251, 251, 251), outline=(214, 216, 215), width=1)
draw_ellipse(636, 500.5, 4, 4, (31, 178, 62))
# enable3d chip
d.rounded_rectangle([227, 262, 264, 276], radius=7, fill=(255, 255, 255), outline=(233, 233, 233), width=1)

rec = np.array(canvas).astype(int)

# ---- compare in regions that should contain only these elements ----
def region_report(name, x0, y0, x1, y1):
    o = orig[y0:y1, x0:x1]
    r = rec[y0:y1, x0:x1]
    # pixels where original is non-white
    mask = (o < 250).any(axis=2)
    n = mask.sum()
    if n == 0:
        print(f"{name}: original empty"); return
    err = np.abs(o.astype(int) - r.astype(int)).mean(axis=2)
    mean_err = err[mask].mean()
    # count of original non-white px missing in rec (rec white there)
    miss = ((r > 250).all(axis=2) & mask).sum()
    # count of rec non-white px where original white
    extra = ((o > 250).all(axis=2) & (r < 250).any(axis=2)).sum()
    print(f"{name}: origNonWhite={n} meanErr={mean_err:5.1f} missing={miss} extra={extra}")

region_report("navbar-left(icons)", 0, 0, 70, 30)
region_report("navbar-right(currencies)", 520, 0, 635, 30)
region_report("pill", 260, 20, 350, 45)
region_report("hairline", 0, 28, 680, 40)
region_report("palette", 95, 404, 224, 510)
region_report("create-btn", 575, 50, 665, 82)
region_report("page-chips", 418, 334, 526, 362)
region_report("dividers", 250, 370, 650, 380)
region_report("remove-btns", 315, 420, 640, 448)
region_report("online-chip", 618, 488, 680, 510)
region_report("enable3d", 220, 256, 270, 282)
