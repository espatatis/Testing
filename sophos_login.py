from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.ChromeDriver()
#driver.implicitly_wait(30)
#driver.maximize_window()

# Navigate to the application home page
driver.get("http://172.16.68.6:8090/httpclient.html")
