from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Firefox()
driver.get('https://facebook.com')
emailelement=driver.find_element(By.XPATH,'.//*[@id-"email"]')
emailelement.send_keys('yi.trevelle@lvory.org')
passelement=driver.find_element(By.XPATH,'.//*[@id-"pass"]')
passelement.send_keys('demousertest123')

elem=driver.find_element(By.XPATH,'.//*[@id-"loginbutton"]')
elem.click()

statuselement=driver.find_element(By.XPATH,"//*[@name='xhpc_message']")
time.sleep(5)
statuselement.send_keys('hi there')
time.sleep(5)
buttons=driver.find_elements_by_tag_name('button')
time.sleep(5)
for button in buttons:
    if buttons.text == 'Post':
        button.click()