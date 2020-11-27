# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
 @file: setup.py
 @Author: Christo
 @time: 2020/11/26 下午8:03
'''


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='json_extract',
    version='1.1.0',
    author='lsl',
    author_email='952597205@qq.com',
    url='https://github.com/TIM952597205/json_tool',
    description=u'json提取器',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
