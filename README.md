# Project_gutenberg

Project Structure

Project_gutenberg
├── README.md                   ← 使用說明
├── request.txt                 ← 環境設置
├─gutenberg_scraper/
│  └─main.py                    ← 主程式
│    browser_setup.py           ← 設定並回傳 Selenium WebDriver
│    language_page.py           ← 導覽到中文頁面、抓取中文書籍清單 
│    book_downloader.py         ← 處理書籍下載連結擷取與檔案儲存
│    dealname.py                ← 檔名處理
