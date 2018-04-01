import time
import random
from selenium import webdriver
from config import COOKIES

def get_driver():
    url = 'https://tieba.baidu.com/index.html'
    # driver = webdriver.PhantomJS()
    # driver = webdriver.PhantomJS('./phantomjs')
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    return driver

def post_tei(driver, url, content):
    driver.delete_all_cookies()
    cookie = COOKIES.pop()
    for i in cookie:
        driver.add_cookie(i)

    driver.get(url)
    time.sleep(2.5)

    driver.find_element_by_xpath('/html/body/ul/li[2]/a').click()
    time.sleep(2.5)

    driver.find_element_by_xpath('//*[@id="ueditor_replace"]').send_keys(content)
    driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[3]/div/a').click()

    newCookie = driver.get_cookies()
    COOKIES.append(newCookie)

    return True
