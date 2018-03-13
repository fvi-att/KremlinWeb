#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def main():
   setup(
       name='kremlin-web',
       version='0.0.1',
       zip_safe=False,
       packages=[],
       install_requires=[
           'flask==0.12.2',
       ],
       dependency_links=[]
   )


if __name__ == '__main__':
   main()