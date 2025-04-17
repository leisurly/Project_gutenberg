# 操作 browser 的 API
from selenium import webdriver

def set_browser():  
    # 啟動瀏覽器工具的選項
    my_options = webdriver.ChromeOptions()
    # my_options.add_argument("--headless")               #不開啟實體瀏覽器背景執行
    my_options.add_argument("--start-maximized")          #最大化視窗
    my_options.add_argument("--incognito")                #開啟無痕模式
    my_options.add_argument("--disable-popup-blocking")   #禁用彈出攔截
    my_options.add_argument("--disable-notifications")    #取消 chrome 推播通知
    my_options.add_argument("--lang=zh-TW")               #設定為正體中文

    # 使用 Chrome 的 WebDriver
    # my_service = Service(executable_path="./chromedriver.exe")
    driver = webdriver.Chrome(options = my_options,
    #     service = my_service
    )
    # 開啟 gutenberg 首頁
    driver.get("https://www.gutenberg.org/")
    return driver