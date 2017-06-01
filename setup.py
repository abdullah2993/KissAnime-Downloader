#!/usr/bin/python
"""
Setup file for KissAnime_DL
"""
from setuptools import setup

setup(
    name='KissAnime Downloader',
    version='0.1.1',
    scripts=['kissanime_dl.py'],
    description='Download anime episodes from KissAnime',
    author='Abdullah Saleem',
    author_email='a.saleem2993@gmail.com',
    url='https://github.com/Abdullah2993/KissAnime-Downloader',
    license='MIT',
    keywords=['kissanime', 'download', 'downloader', 'anime', 'video'],
    install_requires=['beautifulsoup4', 'cfscrape', 'wget']
)