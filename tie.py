import time
from selenium import webdriver

def get_driver():
    return webdriver.Chrome('./chromedriver')

def vote(driver):
    driver.delete_all_cookies()

    driver.get('https://www.shixiseng.com/hirer/eachhirer?com=com_thfa4ld7grt5&award_type=%E6%9C%80%E4%BD%B3%E5%AE%9E%E4%B9%A0%E9%9B%87%E4%B8%BB')

    time.sleep(1)

    driver.find_element_by_css_selector('.vote').click()

    time.sleep(0.5)

    driver.find_element_by_css_selector('.vote').click()

    time.sleep(1)

    return True
