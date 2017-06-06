from distutils.core import setup

import py2exe
# setup(console=["mainwindow.py"])
setup(windows=[{"script":"mainwindow.py"}], options={"py2exe":{"includes":["sip","win_inet_pton"],"bundle_files": 1}})