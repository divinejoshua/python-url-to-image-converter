import asyncio
from pyppeteer import launch

async def create_pdf(url, pdf_path):
  browser = await launch()
  page = await browser.newPage()

  await page.goto(url)
  await page.pdf({'path': pdf_path, 'format': 'A4'})
  await browser.close()

# Run create_pdf
asyncio.get_event_loop().run_until_complete(create_pdf('https://www.google.com/search?q=Who+is+divine&sca_esv=341fc45e8ec89d31&sxsrf=ADLYWIKoEQM_Et2BYKoCU4Dj6Hflkm0xJg%3A1728817028293&source=hp&ei=hKcLZ_KnEL2hhbIP1Oap6Ag&iflsig=AL9hbdgAAAAAZwu1lMUmaXorMS4Q7KozDP20X9cTCxOQ&ved=0ahUKEwjy-eemmYuJAxW9UEEAHVRzCo0Q4dUDCBg&uact=5&oq=Who+is+divine&gs_lp=Egdnd3Mtd2l6Ig1XaG8gaXMgZGl2aW5lMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEinD1AAWPANcAB4AJABAJgBYKABvAeqAQIxM7gBA8gBAPgBAZgCDaAC6wfCAgQQIxgnwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIQEAAYgAQYsQMYQxiDARiKBcICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIOEAAYgAQYsQMYgwEYigXCAgQQABgDmAMAkgcEMTIuMaAHiVc&sclient=gws-wiz', 'google_example.pdf'))