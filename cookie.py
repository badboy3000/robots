from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://tieba.baidu.com/index.html')
driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()


print('请登录')
time.sleep(30)
print('获取cookie')
print(driver.get_cookies())

