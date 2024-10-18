import asyncio
from pyppeteer import launch
import time
async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    # await page.goto('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')
    await page.goto('https://www.g2.com/products/azure-sql-database/reviews')
    time.sleep(10)
    await page.screenshot({'path': 'screen.png', 'fullPage': True})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())