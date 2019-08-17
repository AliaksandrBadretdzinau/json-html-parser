import shutil as sh
from os import path


src = '/usr/local/lib/python3.7/site-packages'
dest = 'layers/JsonPdfEnginePath/python/lib/python3.7/site-packages'
libs = (
    'appdirs.py',
    'pybars',
    'pyee',
    'pymeta',
    'pyppeteer',
    'tqdm',
    'urlib3',
    'websockets'
)

for lib in libs:
    sh.copy(path.join(src, lib), dest)

