import shutil as sh
import os
import sys
#import stat


src = '/usr/local/lib/python3.7/site-packages'
dest = 'layers/JsonPdfEnginePath/python/lib/python3.7/site-packages'
libs = (
    'appdirs.py',
    'pybars',
    'pyee',
    'pymeta',
    'pyppeteer',
    'tqdm',
    'urllib3',
    'websockets'
)
file = os.path.join(dest, 'JsonPdfEngineLayer.py')
#st = os.stat(file)
#os.chmod(file, st.st_mode | stat.S_IEXEC)

for lib in libs:
    obj = os.path.join(src, lib)
    if os.path.isdir(obj):
        sh.copytree(obj, os.path.join(dest, lib))
    else:
        sh.copy(obj, dest)

my_dir = os.path.dirname(dest)
os.system('%s %s' % ('python ', file))
