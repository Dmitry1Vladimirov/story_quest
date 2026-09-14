#!/usr/bin/env python3
"""Генерирует stories/stories.json по файлам в stories/."""
import json
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
STORIES_DIR = os.path.join(HERE, "stories")
MANIFEST = os.path.join(STORIES_DIR, "stories.json")

def load_title(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("title", os.path.splitext(os.path.basename(path))[0])
    except Exception:
        return os.path.splitext(os.path.basename(path))[0]

def make():
    files = sorted(glob.glob(os.path.join(STORIES_DIR, "*.json")))
    items = []
    for f in files:
        name = os.path.basename(f)
        if name == "stories.json":
            continue
        items.append({
            "file": name,
            "title": load_title(f),
        })
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"Готово: {len(items)} шт. → {MANIFEST}")

if __name__ == "__main__":
    make()