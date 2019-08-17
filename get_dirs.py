import shutil as sh


packages = '/usr/local/lib/python3.7/site-packages/'
sourses = '/layers/JsonPdfEnginePath/python/lib/python3.7/site-packages/'

sh.copy(f'{packages}appdir.py', sourses)
