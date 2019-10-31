from selenium import webdriver

# create a new Firefox session
driver = webdriver.ChromeDriver()

# Navigate to the application home page
driver.get("http://172.16.68.6:8090/httpclient.html")
