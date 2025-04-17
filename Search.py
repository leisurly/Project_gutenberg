from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from check import check_chinese_book
from Set_browser import set_browser  


def search():
    driver = set_browser()
    #搜索結果的CSS selector
    cssSelector = "li.booklink > a[href]"
    chinese_book = []
    i = 0
    while True:
        if i == 0:
            url = f"https://www.gutenberg.org/ebooks/search/?query=Chinese&submit_search=Go%21"
        start_index = 26 + 25 * (i - 1)
        url = f"https://www.gutenberg.org/ebooks/search/?query=Chinese&submit_search=Go%21&start_index={start_index}"
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))                      
            results = driver.find_elements(By.CSS_SELECTOR, cssSelector)
            if not results:
                print(f"沒有更多結果，第 {i} 頁為最後一頁。")
                break
            for book in results:
                title = book.text
                chinese_title = check_chinese_book(title)
                if chinese_title:
                    link = book.get_attribute("href")
                    chinese_book.append((title, link))
                    print(f"書名: {chinese_title}, 連結: {link}")
            i += 1  # 下一頁
            print(f"總共抓取 {len(chinese_book)} 本書")
        except TimeoutException:
            print(f"第 {i} 頁載入逾時，跳過。")
            break
    return (chinese_book)