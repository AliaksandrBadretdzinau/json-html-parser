import asyncio
from os import walk
from os.path import join
from pathlib import Path
from pybars import Compiler
from json import load, dumps
from pyppeteer import launch
from functools import lru_cache


HTML_CONF = {
    "ext": ".hbs",
    "layouts_dir": "layouts",
    "partials_dir": "components"
}

PDF_CONF = {
    "path": "result.pdf",
    "printBackground": True,
    "format": "A4"
}

BROWSER = {
    'executablePath': 'chrome-linux/chrome'
}


def html_conf(html_conf):
    HTML_CONF = html_conf


def pdf_conf(pdf_conf):
    PDF_CONF = pdf_conf


def files():
    for r, d, f in walk(HTML_CONF['partials_dir']):
        for file in f:
            if HTML_CONF['ext'] in file:
                yield join(r, file)


def file_read(file):
    with open(file) as f:
        return f.read()


def name(file): return Path(file).stem


def data_compile(file):
    data_source = file_read(file)
    return Compiler().compile(data_source)


@lru_cache(maxsize=128)
def partials_build():
    return {
        'partials': {name(file): data_compile(file) for file in files()}
    }


@lru_cache(maxsize=128)
def template_build(layout_name):
    file = join(HTML_CONF['layouts_dir'], layout_name + HTML_CONF['ext'])
    
    template = data_compile(file)
    partials = partials_build()
    
    return lambda data: template(data, **partials)


async def pdf_build(html):
    browser = await launch()
    page = await browser.newPage()
    await page.setContent(html)
    await page.pdf(PDF_CONF)
    await browser.close()


if __name__ == '__main__':
    with open('data.json') as f:
        data = load(f)

    template = template_build(data['data']['layout_name'])
    html = template(data['data'])

    asyncio.run(pdf_build(html))
