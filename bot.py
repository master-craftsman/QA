from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome('G:/chromedriver.exe')
browser.implicitly_wait(60)
browser.get("https://web.telegram.org")
time.sleep(3)
browser.find_element_by_css_selector('body > div> div > div> div> form > div> div> input').send_keys('9279524819')
time.sleep(3)
browser.find_element_by_css_selector('body > div> div > div> div> div > a > my-i18n').click()
time.sleep(10)
browser.find_element_by_css_selector('body > div> div> div > div > div> button.btn.btn-md.btn-md-primary > span').click()
time.sleep(20)
browser.get("https://web.telegram.org/#/im?p=@dvpe9rkjdijdsabot")
time.sleep(5)
for i in range(0,1000000,1):
 browser.find_element_by_css_selector('body > div > div > div > div> div> div > div> div > div > div > div > form > div > div > div > div > div > div > div > div:nth-child(1) > div:nth-child(1) > button').click()
 browser.find_element_by_css_selector('body > div > div> div > div> div> div > div> div> div > div> div> div > div> div > div > div > div > div > div> div > div > div:nth-child(3) > div > button').click()
 time.sleep(5420)