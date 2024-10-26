from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions
from PIL import Image
import time
import base64

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')

RATIO_MULTIPLIER = 2.5352112676056335

# Function to find page size
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)

# Scale for PDF size. 1 for no change takes long time
pdf_scaler = 0.1


# Find full page dimensions regardless of scroll
height = S('Height')
weight = S('Width')

# Dynamic setting of PDF page dimensions
print_options = PrintOptions()
print_options.page_height = (height*pdf_scaler)*RATIO_MULTIPLIER
print_options.page_width = (weight*pdf_scaler)*RATIO_MULTIPLIER
print_options.shrink_to_fit = True

# Prints to PDF (returns base64 encoded data. Must save)
pdf = driver.print_page(print_options=print_options)
driver.close()

# save the output to a file.
with open('example.pdf', 'wb') as file:
    file.write(base64.b64decode(pdf))