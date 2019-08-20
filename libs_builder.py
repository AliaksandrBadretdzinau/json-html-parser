import shutil as sh
import os
import sys


def copy_libs(src, dest, libs):
    for lib in libs:
        obj = os.path.join(src, lib)
        if os.path.isdir(obj):
            sh.copytree(obj, os.path.join(dest, lib))
        else:
            sh.copy(obj, dest)


def libs_standart():
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
        'pyphen',
        'pycparser',
    )

    copy_libs(src, dest, libs)


def pango():
    src = '/usr/lib/x86_64-linux-gnu'
    dest = sys.argv[0]

    libs = (
        'libpango-1.0.so.0',
        'libpango-1.0.so.0.4000.14',
        'libpangocairo-1.0.so.0',
        'libpangocairo-1.0.so.0.4000.14',
        'libpangoft2-1.0.so.0',
        'libpangoft2-1.0.so.0.4000.14'
    )

    print(dest)
    sh.copy('/usr/lib/x86_64-linux-gnu/libpango-1.0.so.0.4000.14', os.path.join(dest, 'pango-1.0'))
    sh.copy('/usr/lib/x86_64-linux-gnu/libpangocairo-1.0.so.0.4000.14', os.path.join(dest, 'pangocairo-1.0'))
    sh.copy('/usr/lib/x86_64-linux-gnu/libpangoft2-1.0.so.0.4000.14', dest)
    #copy_libs(src, dest, libs)


if __name__ == '__main__':
    libs_standart()
    #pango()
