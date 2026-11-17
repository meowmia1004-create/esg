# ESG 電信品牌認同 Wiki 索引

> 本索引是 Wiki 的入口。每次新增來源或知識頁面後，請同步更新本檔。

## 概念與理論
- [ESG 基本概念](cards/01-esg-basics.md)：整理 E、S、G 三構面的基本意義。
- [電信產業 ESG](cards/02-telecom-esg.md)：整理電信業者的永續議題。
- [品牌認同與消費者－企業認同](cards/04-brand-identification.md)：整理消費者認同概念。
- [CSR 與消費者認同](cards/05-csr-and-identification.md)：整理 CSR 與認同相關研究。

## 個案
- [中華電信回收與循環經濟](cards/03-chunghwa-recycling.md)：整理舊手機回收、綠色換機等個案。

## 專案管理
- [來源清單](sources.md)：記錄預計蒐集與匯入的資料。
- [簡報大綱](outline.md)：教學型 HTML 簡報規劃。
- [執行紀錄](log.md)：依日期追加 ingest、query、lint 記錄。

## 維護規則
- 依照 [AGENTS.md](AGENTS.md) 維護 Wiki。
- 新增資料時使用 [.agents/workflows/ingest.md](.agents/workflows/ingest.md)。
- 定期使用 [.agents/workflows/lint.md](.agents/workflows/lint.md) 與 `python3 scripts/check_wiki.py` 檢查。
