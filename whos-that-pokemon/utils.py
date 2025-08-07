# utils.py
# Utilities: silhouette creation and name normalization

import os
import json
from PIL import Image, ImageOps, ImageFilter
import random
import re

SPRITE_DIR = "assets/sprites"
META_FILE = "assets/names.json"

def load_names():
    if os.path.exists(META_FILE):
        with open(META_FILE, "r") as f:
            d = json.load(f)
        return d
    # fallback: try to build mapping from file names
    mapping = {}
    for fname in os.listdir(SPRITE_DIR):
        if fname.endswith(".png"):
            pid = os.path.splitext(fname)[0]
            mapping[pid] = pid
    return mapping

def create_silhouette(input_path, output_size=(256,256), blur=False):
    """
    Loads a sprite, scales it, and returns a PIL Image with a black silhouette
    (transparent background).
    """
    img = Image.open(input_path).convert("RGBA")

    # Resize preserving aspect
    img = ImageOps.contain(img, output_size)

    # Create silhouette: black pixels where alpha > 0
    w, h = img.size
    silhouette = Image.new("RGBA", (w, h), (0,0,0,0))
    px = img.load()
    s_px = silhouette.load()
    for x in range(w):
        for y in range(h):
            r, g, b, a = px[x,y]
            if a > 20:  # threshold
                s_px[x,y] = (0, 0, 0, 255)
            else:
                s_px[x,y] = (0, 0, 0, 0)

    if blur:
        silhouette = silhouette.filter(ImageFilter.GaussianBlur(radius=1))

    # Pad to output_size centered
    bg = Image.new("RGBA", output_size, (0,0,0,0))
    bx = (output_size[0] - w) // 2
    by = (output_size[1] - h) // 2
    bg.paste(silhouette, (bx, by), silhouette)
    return bg

def normalize_name(name):
    """Lowercase, remove non-alpha, common punctuation, handle spaces/dashes"""
    name = name.lower()
    name = re.sub(r"[^a-z0-9]", "", name)
    return name

def random_pokemon_ids(n=1):
    ids = [str(i) for i in range(1, 152)]
    return random.sample(ids, n)