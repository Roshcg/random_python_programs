from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/home/m1049296/Desktop/rosh/chromedriver')
# driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"Twilio"'

# Replace the below string with your own message
string = "Message was deleted"

x_arg = '//span[contains(@title,' + target + ')]'
print('1')
print('2')
# user = driver.find_element_by_css_selector('//span[contains(@title,' + target + ')]')
# user.click()
# print(user)

group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
print('3')

# inp_xpath = '//*[@id="main"]/footer/div[0]/div[1]/div/div[1]'
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
# input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
input_box = driver.find_elements_by_css_selector('#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text')
print('4')

print(input_box)
time.sleep(1)