import shutil as sh
from os import path


packages = '/usr/local/lib/python3.7/site-packages'
sourses = 'layers/JsonPdfEnginePath/python/lib/python3.7/site-packages'

sh.copy(path.join(packages, 'appdirs.py'), sourses)
