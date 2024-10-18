from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')
time.sleep(3)
driver.save_full_page_screenshot('fullpage_gecko_firefox.png')
driver.quit()
