from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://inventwithpython.com')
print(driver.title)
# 'Invent with Python'

driver.quit()