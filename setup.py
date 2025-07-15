from setuptools import setup, find_packages
import os

import re, ast

# get version from __version__ variable in app's/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('branded_lms/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
    name='branded_lms',
    version=version,
    description='App for LMS',
    author='Tim',
    author_email='revant.one@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)