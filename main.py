from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from Set_browser import set_browser  
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from download import download




driver = set_browser()

# 找到搜尋框並輸入文字
inputElement = driver.find_element(By.CSS_SELECTOR, 'input#menu-book-search')
inputElement.send_keys("Chinese")
sleep(2)
inputElement.submit()
download()  


driver.quit()

