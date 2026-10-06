# -*- coding: utf-8 -*-
"""pack/ 以下を Godot 4.5 形式(v3)のPCKにまとめ、dist/HermitMod_JPN/ に出力する"""
import hashlib, json, os, re, struct, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PACK = os.path.join(ROOT, "pack")
DIST = os.path.join(ROOT, "dist", "HermitMod_JPN")
MOD_ID = "HermitMod_JPN"

# 英語版との整合チェック(任意): 引数にengフォルダを渡す
if len(sys.argv) > 1:
    eng = sys.argv[1]
    for f in ["cards", "powers", "relics", "ancients", "characters", "card_keywords"]:
        e = json.load(open(os.path.join(eng, f + ".json"), encoding="utf-8"))
        j = json.load(open(os.path.join(PACK, "HermitMod", "localization", "jpn", f + ".json"), encoding="utf-8"))
        print(f, "missing:", [k for k in e if k not in j], "extra:", [k for k in j if k not in e])
        for k in e:
            if k in j:
                a = re.findall(r"\{(\w+)", e[k])
                for name in a:
                    if name not in j[k]:
                        print("  placeholder missing:", k, name)

files = []
for dp, _, fns in os.walk(PACK):
    for fn in fns:
        full = os.path.join(dp, fn)
        rel = os.path.relpath(full, PACK).replace("\\", "/")
        files.append(("res://" + rel, open(full, "rb").read()))
files.sort()

entries = b""
dir_size = 4
for path, data in files:
    pb = path.encode("utf-8") + b"\0"
    pb += b"\0" * ((4 - len(pb) % 4) % 4)
    dir_size += 4 + len(pb) + 8 + 8 + 16 + 4
header_size = 40
data_off = header_size + dir_size
directory = struct.pack("<I", len(files))
blob = b""
for path, data in files:
    pb = path.encode("utf-8") + b"\0"
    pb += b"\0" * ((4 - len(pb) % 4) % 4)
    directory += struct.pack("<I", len(pb)) + pb
    directory += struct.pack("<QQ", data_off + len(blob), len(data))
    directory += hashlib.md5(data).digest() + struct.pack("<I", 0)
    blob += data
header = b"GDPC" + struct.pack("<IIII", 3, 4, 5, 1) + struct.pack("<IQQ", 0, 0, header_size)
assert len(header) == header_size
os.makedirs(DIST, exist_ok=True)
with open(os.path.join(DIST, MOD_ID + ".pck"), "wb") as f:
    f.write(header + directory + blob)
manifest = {
    "id": MOD_ID,
    "name": "The Hermit 日本語化",
    "author": "danli",
    "description": "The Hermit MODの日本語ローカライズ(カード・レリック・パワー・キーワード・建築家との会話)。",
    "version": "v1.0.0",
    "has_pck": True,
    "has_dll": False,
    "dependencies": [{"id": "HermitMod", "min_version": "v1.5.0"}],
    "affects_gameplay": False,
}
with open(os.path.join(DIST, MOD_ID + ".json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("built", len(files), "files,", os.path.getsize(os.path.join(DIST, MOD_ID + ".pck")), "bytes")
