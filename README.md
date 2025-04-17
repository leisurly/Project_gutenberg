## 📁 Project Structure

```markdown
Project_gutenberg
├── main.py                   ← 程式入口：搜尋並下載書籍
├── download.py               ← 負責下載書籍內容與儲存為 txt
├── Search.py                 ← 搜尋中文書籍並擷取連結與書名
├── check.py                  ← 工具函式：清洗書名與中文內容
├── Set_browser.py            ← 瀏覽器自動化設定（Selenium）
├── README.md                 ← 📘 使用說明與執行步驟
├── requirements.txt          ← ⚙️ 環境依賴清單（安裝套件用）
└── project_gutenberg/        ← 📂 儲存下載下來的 txt 書籍檔案
