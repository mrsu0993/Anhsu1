# This file is imported from __init__.py and exec'd from setup.py

MAJOR = 3
MINOR = 0
MICRO = 0
RELEASE = False

__version__ = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

if not RELEASE:
    # if it's a rcx release, it's not proceeded by a period. If it is a
    # devx release, it must start with a period
    __version__ += '.dev0'


_kivy_git_hash = ''
_kivy_build_date = ''
