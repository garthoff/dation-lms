from setuptools import setup, find_packages

setup(
    name='branded_lms',
    version='1.0.0',
    description='Frappe LMS with custom branding support',
    author='Tim Garthoff',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
