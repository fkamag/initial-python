from time import sleep
from selenium import webdriver

firefox = webdriver.Firefox()

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--start-maximized')

response = firefox.get('https://www.google.com/')

sleep(5)
firefox.quit()