#!/usr/bin/env python3

from setuptools import setup

setup(name='PY YT Downloader',
      version='1.1',
      description='Youtube video downloader written in pure Python. Powered by pytube3.',
      author='Gabriel D. Sanchez',
      author_email='gabriel.duarte.sanchez@gmail.com',
      url='',
      packages=['yt_video_downloader'],
      install_requires=[
        'pytube==11.0.1',
    ],
      data_files=[('bitmaps', ['icons/folder-24px.png'])],
     )