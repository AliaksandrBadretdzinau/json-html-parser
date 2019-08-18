import asyncio
from pyppeteer import launch

PDF_CONF = {
    "path": "result.pdf",
    "printBackground": True,
    "format": "A4"
}

BROWSER = {
    'args': ['--no-sandbox']
}

async def pdf_build(html):
    browser = await launch(BROWSER)
    page = await browser.newPage()
    await page.setContent(html)
    await page.pdf(PDF_CONF)
    await browser.close()


if __name__ == "__main__":
    html = '<h1>Test</h1>'
    asyncio.run(pdf_build(html))
