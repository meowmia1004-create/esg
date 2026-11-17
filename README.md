# ESG 永續策略對電信消費者品牌認同之影響

本專案以台灣電信產業為情境，整理 ESG（環境、社會、公司治理）、中華電信永續措施，以及消費者－企業認同相關理論，並以 Wiki 知識卡片作為教學型 HTML 簡報的主要知識來源。

## 專案內容
- `sources.md`：資料來源與用途
- `cards/`：整理後的知識卡片
- `outline.md`：教學簡報大綱
- `drafts/`：逐頁內容草稿
- `deck.html`：可離線開啟的教學型 HTML 簡報
- `AGENTS.md`：AI 執行規則
- `.agents/workflows/topic-slides.md`：Graph / Loop 工作流程
- `report.md`：執行檢查紀錄與反思表（請依實際操作填寫）

## 使用方式
1. 先閱讀 `sources.md`，下載或開啟資料來源。
2. 將來源文件匯入老師指定的 LLM Wiki，至少完成 5 篇 Ingest。
3. 依照 `cards/` 的分類整理 Wiki 知識卡片。
4. 依照 `.agents/workflows/topic-slides.md` 執行流程。
5. 開啟 `deck.html` 預覽簡報。這份 HTML 是可用的初始成果；若要證明「由 Wiki 生成」，仍須在指定平台實際執行並保留紀錄。
6. 完成實測後，更新 `report.md`，附上 Wiki URL、GitHub URL 與實際截圖。

## GitHub 上傳（最簡單方式）
在 GitHub 建立一個新的 Public 或 Private Repository，名稱可用 `esg-telecom-wiki`。將本資料夾內所有檔案上傳。若使用 Git 指令：

```bash
git init
git add .
git commit -m "Initial ESG telecom Wiki project"
git branch -M main
git remote add origin https://github.com/你的帳號/esg-telecom-wiki.git
git push -u origin main
```

將 `你的帳號` 換成自己的 GitHub 使用者名稱。不要把密碼、API Key 或私人資料放進 Repository。
