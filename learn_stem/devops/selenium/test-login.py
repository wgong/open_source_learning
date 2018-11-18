# https://www.guru99.com/selenium-python.html#5

from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
browser = webdriver.Firefox()
browser.get("http://www.facebook.com")
  
username = browser.find_element_by_id( "email" )
password = browser.find_element_by_id( "pass" )
submit   = browser.find_element_by_id( "loginbutton"   )
  
username.send_keys( "me" )
password.send_keys( "mykewlpass" )
submit.click()
  
"""
wait = WebDriverWait( browser, 5 )
  
try:
	page_loaded = wait.until_not(
	lambda browser: browser.current_url == login_page
)
except TimeoutException:
	print("Timeout")
"""
	
webdriver.quit()