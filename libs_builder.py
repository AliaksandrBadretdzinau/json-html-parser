import shutil as sh
import os
import sys
#import stat


src = '/usr/local/lib/python3.7/site-packages'
dest = 'layers/JsonPdfEnginePath/python/lib/python3.7/site-packages'
libs = (
    'pybars',
    'pymeta',
    'weasyprint',
    'cssselect2',
    'webencodings',
    'tinycss2',
    'html5lib',
    'cairocffi',
    'cffi',
    '_cffi_backend.cpython-37m-x86_64-linux-gnu.so',
    '.libs_cffi_backend',
    'pyphen'
)

for lib in libs:
    obj = os.path.join(src, lib)
    if os.path.isdir(obj):
        sh.copytree(obj, os.path.join(dest, lib))
    else:
        sh.copy(obj, dest)
