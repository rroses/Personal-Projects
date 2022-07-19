from lib2to3.pgen2 import driver
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import pyautogui as pag
import time
import pyfiglet

banner = pyfiglet.figlet_format("phish v1.0")
print(banner)
print("-" * 30)
username = input("Enter Username/Email: ")
password = getpass()

targets = ['c.a.test.2500@gmail.com']


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# Go to target website (AOL Email)
driver.get("https://login.aol.com/?src=fp-us&client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&crumb=MuLZX7Fg7Zl&intl=us&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&pspid=1197803361&activity=default&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkbX1xprFR8HA1mul1nNast6hxwlrksan%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E")

time.sleep(2)

# Enter username
driver.find_element_by_id("login-username").send_keys(username)
driver.find_element_by_id("login-signin").click()

time.sleep(2)

# Enter password
driver.find_element_by_id("login-passwd").send_keys(password)
driver.find_element_by_id("login-signin").click()

time.sleep(4)

# Go to mail address
driver.get("https://mail.aol.com/webmail-std/en-us/suite")
#pag.moveTo(297, 230)
#pag.click()

time.sleep(4)

# Open Email Composition
pag.moveTo(80, 215, 0.5)
pag.click()

time.sleep(2)

for target in targets:
    # Enter the target email
    pag.moveTo(226, 284, 0.3)
    pag.click()
    pag.typewrite(target, 0.1)

    # Enter the Subject
    pag.moveTo(272, 320, 0.3)
    pag.click()
    pag.typewrite("YOU WON!!!", 0.1)

    # Enter the Body
    pag.moveTo(214, 413, 0.3)
    pag.click()
    pag.typewrite("CONGRATULATIONS! Please fill out the attached document to claim your prize!", 0.1)

    # Attach the .exe file
    pag.moveTo(396, 212, 0.3)
    pag.click()
    pag.moveTo(237, 116, 0.3)
    pag.click()
    pag.moveTo(372, 141, 0.3)
    pag.click()
    pag.moveTo(1138, 702, 0.3)
    pag.click()

    # Send the email
    pag.moveTo(220, 205, 0.3)
    pag.click()

    time.sleep(2)

    # Go Back to Compose
    pag.moveTo(80, 210, 0.3)
    pag.click()

print("\nSession Terminated.")


