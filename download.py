import requests as req
import os
import re
from bs4 import BeautifulSoup as bs
from Search import search 
from check import extract_chinese_sentences, split_by_length

def download():
    folderPath = 'project_gutenberg'
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    list_chinese_book = search()  # 格式：[("書名", "https://www.gutenberg.org/ebooks/XXXXX")]

    for title, url in list_chinese_book:
        try:
            res = req.get(url)
            soup = bs(res.text, "lxml")
            # 檢查是否標示為中文語言
            is_chinese = soup.find("a", href="/browse/languages/zh") is not None
            if not is_chinese:
                print(f"略過（非標示中文語言）: {title}")
                continue
            # 找到下載連結（Plain Text UTF-8）
            #<https://www.gutenberg.org/cache/epub/23962/pg23962.txt>
            #<a href="/ebooks/23962.txt.utf-8" type="text/plain; charset=us-ascii" class="link " title="Download">Plain 
            link_tag = soup.find("a", href=lambda x: x and "txt" in x)
            if link_tag is not None:
                print(type(link_tag))  # <class 'bs4.element.Tag'>
                print(link_tag["href"])  # 抓出連結
            download_url = "https://www.gutenberg.org" + link_tag["href"]
            response = req.get(download_url)
            # 只保留中文字作為檔名
            safe_title = re.sub(r'[^\u4e00-\u9fff]', '', title)
            filename = f"{safe_title}.txt"
            filepath = os.path.join(folderPath, filename)
            text = response.text
            #檔案內容全部中文
            sentences = extract_chinese_sentences(text)
            #把抓取內容分段顯示
            sentences = split_by_length(sentences,100)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(sentences))
                print(f" 已下載: {title}")
        except Exception as e:
            print(f"發生錯誤：{title} - {e}")
