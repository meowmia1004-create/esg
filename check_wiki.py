#!/usr/bin/env python3
"""檢查 ESG 電信品牌認同 Wiki 的基本完整性。"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors, warnings, passed = [], [], []

def check(condition, ok, bad):
    (passed if condition else errors).append(ok if condition else bad)

check((ROOT / "AGENTS.md").is_file(), "AGENTS.md 存在", "缺少 AGENTS.md")
check((ROOT / "index.md").is_file(), "index.md 存在", "缺少 index.md")
check((ROOT / "log.md").is_file(), "log.md 存在", "缺少 log.md")
check((ROOT / "deck.html").is_file(), "deck.html 存在", "缺少 deck.html")
check((ROOT / ".agents/workflows/ingest.md").is_file(), "Ingest workflow 存在", "缺少 Ingest workflow")
check((ROOT / ".agents/workflows/lint.md").is_file(), "Lint workflow 存在", "缺少 Lint workflow")

cards = sorted((ROOT / "cards").glob("*.md")) if (ROOT / "cards").exists() else []
check(len(cards) >= 5, f"知識卡片數量：{len(cards)}（至少 5）", f"知識卡片只有 {len(cards)} 張，少於 5 張")

for card in cards:
    content = card.read_text(encoding="utf-8")
    check(bool(re.search(r"(?m)^#\s+.+", content)), f"{card.name} 有標題", f"{card.name} 缺少 Markdown 標題")
    if not re.search(r"來源|參考|DOI|http", content, re.I):
        warnings.append(f"{card.name} 尚未辨識到來源線索，請人工確認")

# Check local Markdown links in index and cards
md_files = [ROOT / "index.md"] + cards
for md in md_files:
    if not md.exists():
        continue
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = (md.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            errors.append(f"{md.relative_to(ROOT)} 連結失效：{target}")
        else:
            passed.append(f"{md.relative_to(ROOT)} 連結有效：{target}")

sources = ROOT / "sources.md"
if sources.exists():
    src_text = sources.read_text(encoding="utf-8")
    # The list is a planned source register, not proof that platform ingest occurred.
    count = len(re.findall(r"(?m)^\s*(?:[-*]|\d+\.)\s+", src_text))
    passed.append(f"sources.md 有 {count} 個清單項目（請人工確認至少 5 篇已實際匯入）")
else:
    errors.append("缺少 sources.md")

print("=== ESG LLM Wiki 結構檢查 ===")
for item in passed:
    print("[PASS]", item)
for item in warnings:
    print("[WARN]", item)
for item in errors:
    print("[FAIL]", item)
print(f"\n結果：{len(passed)} PASS / {len(warnings)} WARN / {len(errors)} FAIL")
print("注意：本程式只檢查檔案結構與連結，不代表來源已在指定平台完成 ingest，也不代表內容已通過學術查證。")
sys.exit(1 if errors else 0)
