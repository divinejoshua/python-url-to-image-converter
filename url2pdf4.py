from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from PIL import Image
import time
import os
import io  # Import io module for in-memory byte handling

# Configure Firefox for headless mode
firefox_options = FirefoxOptions()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(options=firefox_options)

# Load the web page
driver.get('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')
driver.maximize_window()
time.sleep(2)  # Allow some time for the page to load completely

# Function to get the full page height
def get_page_height():
    return driver.execute_script('return document.body.scrollHeight')

# Capture screenshots in sections and store them
screenshots = []
current_scroll = 0
page_height = driver.execute_script("return window.innerHeight")  # Viewport height
full_page_height = get_page_height()

# Scroll and capture screenshots
while current_scroll < full_page_height:
    # Capture screenshot and store in list
    screenshot = driver.get_screenshot_as_png()
    screenshots.append(Image.open(io.BytesIO(screenshot)))
    
    # Scroll down
    current_scroll += page_height
    driver.execute_script(f"window.scrollTo(0, {current_scroll});")
    time.sleep(1)  # Give time for page load/scroll effects

# Close the browser
driver.quit()

# Create PDF with each screenshot as a separate page
pdf_pages = []
for screenshot in screenshots:
    pdf_pages.append(screenshot.convert('RGB'))

# Save all images as a multi-page PDF
pdf_pages[0].save("example_multipage.pdf", save_all=True, append_images=pdf_pages[1:])

print("Multi-page PDF created successfully!")
