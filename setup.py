#!./yt_downloader/Scripts/python.exe

from distutils.core import setup

setup(name='PY YT Downloader',
      version='1.0',
      description='Youtube Video Downloader written in pure Python. Powered by pytube3.',
      author='Gabriel D. Sanchez',
      author_email='gabriel.duarte.sanchez@gmail.com',
      url='',
      packages=['yt_downloader'],
      data_files=[('bitmaps', ['icons/folder-24px.png'])],
     )