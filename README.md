# Project Gutenberg 中文書籍下載器

## 📝 功能介紹
本工具會自動使用 Selenium 搜尋 Gutenberg 上標示為「Chinese」的書籍，下載其純文字內容並儲存為 `.txt` 檔案（僅保留中文內容）。

## 🚀 使用方式

1. 安裝套件
```bash
pip install -r requirements.txt
```

2. 執行主程式
```bash
python main.py
```

3. 下載完成的書籍會儲存在 `project_gutenberg/` 資料夾內。

## 📁 專案結構

```
Project_gutenberg
├── main.py
├── download.py
├── Search.py
├── check.py
├── Set_browser.py
├── README.md
├── requirements.txt
└── project_gutenberg/
```

## 📌 注意事項
- 執行需安裝 Chrome 瀏覽器與對應 chromedriver。
- 初次執行請確認是否有開啟網路連線。

## 🧰 開發環境

- **Python 版本**: 3.11+
- **作業系統相容**: Windows / macOS / Linux
- **執行方式**: 本地端執行，需安裝 Chrome 與對應 chromedriver

## 📦 使用套件與建議版本

| Software        | Version   |
|-----------------|-----------|
| selenium        | 4.19.0    |
| requests        | 2.31.0    |
| beautifulsoup4  | 4.12.3    |
| lxml            | 5.1.0     |
