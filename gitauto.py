from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

username = "rroses"
password = "git_hub_test_python"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://github.com/login")

driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()

while True:
    pass