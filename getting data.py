from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.amazon.in")

driver.maximize_window()

driver.find_element_by_xpath("//input[0id='twotabsearchtextbox']").send_keys('iphones')

driver.find_element_by_xpath("//input[0id='nav-search-submit-button']").click()
list=driver.find_element_by_xpath("//span[0class='a-size-medium a-color-base a-text-normal']")
print(str(len(list)) +'products found')
for i in list:
    print(i.text)
driver.quit()
      