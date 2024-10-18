from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image


from selenium import webdriver
import base64

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.g2.com/products/azure-sql-database/reviews")

#get window size
page_rect = driver.execute_cdp_cmd('Page.getLayoutMetrics', {})

# parameters needed for full page screenshot
# note we are setting the width and height of the viewport to screenshot, same as the site's content size
screenshot_config = {
    'captureBeyondViewport': True,
    'fromSurface': True,
    'clip': {
        'width': page_rect['contentSize']['width'],
        'height': page_rect['contentSize']['height'],
         'x': 0,
         'y': 0,
         'scale': 1
    }
}
# Dictionary with 1 key: data
base_64_png = driver.execute_cdp_cmd('Page.captureScreenshot', screenshot_config)

# Write img to file
with open("imageToSave.png", "wb") as fh:
    fh.write(base64.urlsafe_b64decode(base_64_png['data']))

driver.quit()