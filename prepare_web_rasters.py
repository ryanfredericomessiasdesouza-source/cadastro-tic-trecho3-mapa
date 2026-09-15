#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
from collections import deque
from osgeo import gdal
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parent
SRC = Path(os.environ.get('QGIS_RASTER_DIR', ROOT))
items = [
    ('LO_002', SRC / 'odm_orthophoto1.tif'),
    ('LO_003', SRC / 'odm_orthophoto2.tif'),
    ('VA_004', SRC / 'odm_orthophoto.tif'),
]

def bounds_from_extent(extent):
    pts = [p for ring in extent['coordinates'] for p in ring]
    lons = [p[0] for p in pts]
    lats = [p[1] for p in pts]
    return [[min(lats), min(lons)], [max(lats), max(lons)]]

def edge_connected_dark(arr, threshold=40):
    dark = arr.max(axis=2) <= threshold
    h, w = dark.shape
    transparent = np.zeros((h, w), dtype=bool)
    q = deque()
    for x in range(w):
        if dark[0, x]: q.append((0, x))
        if dark[h - 1, x]: q.append((h - 1, x))
    for y in range(h):
        if dark[y, 0]: q.append((y, 0))
        if dark[y, w - 1]: q.append((y, w - 1))
    while q:
        y, x = q.popleft()
        if transparent[y, x] or not dark[y, x]:
            continue
        transparent[y, x] = True
        for yy in range(max(0, y - 1), min(h, y + 2)):
            for xx in range(max(0, x - 1), min(w, x + 2)):
                if not transparent[yy, xx] and dark[yy, xx]:
                    q.append((yy, xx))
    return transparent

manifest = []
for name, src in items:
    ds = gdal.Open(str(src), gdal.GA_ReadOnly)
    if ds is None:
        raise RuntimeError(f'Não foi possível abrir {src}')
    info = gdal.Info(ds, format='json', deserialize=True)
    extent = info['wgs84Extent']
    bounds = bounds_from_extent(extent)
    lon_span = bounds[1][1] - bounds[0][1]
    lat_span = bounds[1][0] - bounds[0][0]
    width = 1200
    height = max(1, round(width * lat_span / lon_span))
    tmp = ROOT / f'.{name}_web_4326.tif'
    out = ROOT / f'{name}_web.webp'
    warped = gdal.Warp(
        str(tmp), ds, format='GTiff', dstSRS='EPSG:4326', width=width, height=height,
        resampleAlg='bilinear', outputType=gdal.GDT_Byte,
        creationOptions=['TILED=YES', 'COMPRESS=DEFLATE', 'BIGTIFF=IF_SAFER'],
        multithread=True,
    )
    if warped is None:
        raise RuntimeError(f'Falha na reprojeção de {src}')
    warped.FlushCache()
    warped = None
    ds = None
    with Image.open(tmp) as im:
        rgb = im.convert('RGB')
        arr = np.asarray(rgb)
        dark = arr.max(axis=2) <= 8
        transparent = edge_connected_dark(arr)
        alpha = np.where(transparent, 0, 255).astype(np.uint8)
        rgba_arr = np.dstack((arr, alpha))
        rgba = Image.fromarray(rgba_arr, 'RGBA')
        rgba.save(out, 'WEBP', quality=88, method=6)
    tmp.unlink(missing_ok=True)
    manifest.append({'id': name, 'file': out.name, 'bounds': bounds, 'size': [width, height], 'bytes': out.stat().st_size})

(ROOT / 'web_rasters.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for row in manifest:
    print(json.dumps(row, ensure_ascii=False))
