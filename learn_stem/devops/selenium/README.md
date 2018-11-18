## Selenium Tutorial

version = 3.141.5

https://www.tutorialspoint.com/selenium/selenium_environment_setup.htm

- install/start selenium-server-standalone-3
	$ java -jar selenium-server-standalone-3.141.5.jar

11:58:08.970 INFO [SeleniumServer.boot] - Selenium Server is up and running on port 4444

- install selenium/python lang binding

	$ pip install selenium
	
- install js binding

	$ npm i selenium-webdriver
	
- install java binding

C:\GitHub\eclipse-workspace\selenium-java

### Selenium WebDriver
https://www.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example


- easy to use python binding

* add geckodriver.exe to os PATH
	copy to /c/zapme/My_Scripts/geckodriver

* add chromedriver.exe
	copy to /c/zapme/My_Scripts/geckodriver


https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
```
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://inventwithpython.com')
```
