from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

username = "carsonmelton5@gmail.com"
password = "test123!"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.facebook.com")

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

while True:
    pass 