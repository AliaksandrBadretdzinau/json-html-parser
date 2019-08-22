import shutil as sh
import os


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
        'fpdf',
        'selenium'
    )

    copy_libs(src, dest, libs)


if __name__ == '__main__':
    libs_standart()
    #pango()
