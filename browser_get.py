from pyppeteer import launch

PDF_CONF = {
    "path": "result.pdf",
    "printBackground": True,
    "format": "A4"
}

BROWSER = {
    'args': ['--no-sandbox']
}

browser = await launch(BROWSER)
page = await browser.newPage()
await page.setContent(html)
await page.pdf(PDF_CONF)
await browser.close()
