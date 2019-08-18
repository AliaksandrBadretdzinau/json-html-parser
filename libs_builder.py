import shutil as sh
import os
import sys
#import stat


src = '/usr/local/lib/python3.7/site-packages'
dest = 'layers/JsonPdfEnginePath/python/lib/python3.7/site-packages'
libs = (
    'pybars',
    'pymeta'
)

for lib in libs:
    obj = os.path.join(src, lib)
    if os.path.isdir(obj):
        sh.copytree(obj, os.path.join(dest, lib))
    else:
        sh.copy(obj, dest)
