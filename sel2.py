from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome('/home/m1049296/Desktop/rosh/chromedriver')
browser.get('https://web.whatsapp.com/')
print('1')
wait = WebDriverWait(browser, 600)
print('2')
target = '""' #enter contact name here
string = "gg" #target msg
x_arg = ' //span[contains(@title, ' + target +')]'

target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
print('3')
target.click()
print('4')
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
# input_box = browser.find_element_by_xpath(inp_xpath)
input_box = wait.until(ec.presence_of_element_located((By.XPATH, inp_xpath)))
print('5')
time.sleep(2)
input_box.send_keys(string + Keys.ENTER)
time.sleep(2)
