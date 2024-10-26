from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from PIL import Image

def get_page_size(driver):
    return driver.execute_script('return [document.documentElement.clientWidth, document.documentElement.clientHeight];')

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def capture_screenshot_as_pdf(driver, file_path):
    driver.save_screenshot(file_path)

def convert_to_pdf(input_file, output_file):
    image = Image.open(input_file)
    image.save(output_file, 'PDF', resolution=100.0)

# Set up the Firefox driver with options
options = Options()
options.headless = True
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['acceptInsecureCerts'] = True
driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install(), capabilities=capabilities)

# Navigate to the webpage
driver.get('https://www.google.com')

# Get the page size
page_size = get_page_size(driver)

# Set the window size
driver.set_window_size(page_size[0], page_size[1])

# Scroll to the bottom to load dynamic content
scroll_to_bottom(driver)

# Capture the full-page screenshot as PNG
png_file_path = 'full_page_screenshot.png'
capture_screenshot_as_pdf(driver, png_file_path)

# Convert the PNG screenshot to PDF
pdf_file_path = 'full_page_screenshot.pdf'
convert_to_pdf(png_file_path, pdf_file_path)

# Clean up and close the browser
driver.quit()