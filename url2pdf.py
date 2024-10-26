import asyncio
from pyppeteer import launch

async def create_pdf(url, pdf_path):
  browser = await launch()
  page = await browser.newPage()

  await page.goto(url)
  await page.pdf({'path': pdf_path, 'format': 'A4'})
  await browser.close()

# Run create_pdf
asyncio.get_event_loop().run_until_complete(create_pdf('https://en.wikipedia.org/wiki/The_World%27s_Billionaires', 'google_example.pdf'))