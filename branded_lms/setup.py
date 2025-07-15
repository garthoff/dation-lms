# Frappe Bench expects this top-level assignment:
version = '0.0.1'

from setuptools import setup, find_packages

setup(
    name='branded_lms',
    version=version,
    description='Branded LMS App',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe']
)
