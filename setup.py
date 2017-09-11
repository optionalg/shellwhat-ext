#!/usr/bin/env python

import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('shellwhat_ext.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
	name = 'shellwhat-ext',
	version = version,
        py_modules= ['shellwhat_ext'],
        install_requires = ['shellwhat'],
        description = 'shellwhat extensions - high level SCTs',
        author = 'Greg Wilson',
        author_email = 'greg@datacamp.com',
        url = 'https://github.com/datacamp/shellwhat-ext')
