# Python 政府開放資料 API 作品集網站

本專案使用 Python 串接 10 項政府開放資料 API，
進行 JSON 資料讀取、欄位整理與 HTML 表格產生，
並將成果整合為可公開瀏覽的作品集網站。

## 線上作品集

[開啟 GitHub Pages 作品集網站](https://guanhaoren667.github.io/python-open-data-portfolio/)

## 專案說明

本專案是「Python 政府開放資料 API 查詢系統」的第二階段成果。

第一階段先將 10 項政府開放資料 API 拆分為獨立 Python 模組，
再透過文字選單整合為統一的查詢系統。

第二階段建立 10 支 Python 網頁產生器，
將 API 回傳的 JSON 資料整理成 HTML 表格，
並製作作品集首頁與 10 個獨立資料頁面。

## 主要功能

1. 串接 10 項政府開放資料 API。
2. 讀取並整理 JSON 資料欄位。
3. 使用 Python 自動產生 10 個 HTML 資料頁面。
4. 由作品集首頁進入各項 API 資料頁。
5. 各資料頁可返回作品集首頁。
6. 在窄螢幕及手機版中，可左右滑動查看完整表格。
7. 重新執行對應產生器，即可重新讀取 API 並更新 HTML 資料。
8. 透過 GitHub Pages 公開發布作品集網站。

## 使用技術

- Python
- requests
- urllib3
- JSON
- HTML
- CSS
- GitHub
- GitHub Pages
- Python 函式與模組匯入
- 例外處理
- HTML 自動產生

## 專案檔案

```text
python-open-data-portfolio/
├── index.html
├── api01.html
├── api02.html
├── api03.html
├── api04.html
├── api05.html
├── api06.html
├── api07.html
├── api08.html
├── api09.html
├── api10.html
├── generate_api01_html.py
├── generate_api02_html.py
├── generate_api03_html.py
├── generate_api04_html.py
├── generate_api05_html.py
├── generate_api06_html.py
├── generate_api07_html.py
├── generate_api08_html.py
├── generate_api09_html.py
├── generate_api10_html.py
├── requirements.txt
└── README.md
```
## 檔案用途

- `index.html`：作品集網站首頁。
- `api01.html`～`api10.html`：各項 API 的資料表頁面。
- `generate_api01_html.py`～`generate_api10_html.py`：讀取 API 資料並產生對應的 HTML 頁面。
- `requirements.txt`：紀錄專案使用的 Python 套件。
- `README.md`：專案說明文件。

## 更新資料方式

1. 安裝專案需要的套件：

```bash
pip install -r requirements.txt
```

2. 執行需要更新的 Python 網頁產生器，例如：

```bash
python generate_api06_html.py
```

3. 程式會重新讀取 API，並更新對應的 HTML 資料頁。

## 相關專案

第一階段的 Python 文字選單查詢系統：

[查看 Python 政府開放資料 API 查詢系統](https://github.com/guanhaoren667/python-government-open-data-menu)

## 開發方式說明

本專案採用 AI 工具輔助開發。

AI 工具協助提供部分程式碼初稿與修改建議；我負責資料來源選擇、需求整理、程式執行、API 欄位檢查、輸出驗證、問題回報、版面調整、跨裝置測試、GitHub 版本管理及 GitHub Pages 公開發布。

AI 產生的程式碼並非未經檢查直接使用，而是經過實際執行、測試與逐步修改後，再整合至專案中。

目前仍持續補強 Python 程式解讀與獨立撰寫能力。

## 已知限制

- GitHub Pages 提供的是靜態網站，不會在訪客開啟網站時即時執行 Python。
- 網頁中的資料來自最近一次執行 Python 產生器時取得的 API 內容。
- 如果政府開放資料 API 的網址或欄位發生變更，可能需要同步修改產生器。
- 部分資料來源在本機環境曾出現 SSL 憑證驗證問題，目前程式採用暫時性相容處理；正式環境仍應優先維持憑證驗證。

## 專案狀態

核心功能已完成，目前持續進行資料更新、內容維護及程式理解練習。
