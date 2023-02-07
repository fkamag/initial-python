from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--start-maximized')

response = firefox.get('https://www.google.com/')

search_input = firefox.find_element('name', 'q')
search_input.send_keys('mister boni')

sleep(2)

search_input.send_keys(Keys.ENTER)

sleep(5)
firefox.quit()