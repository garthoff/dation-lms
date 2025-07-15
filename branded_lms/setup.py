from setuptools import setup, find_packages
setup(
    name='branded_lms',
    version='0.0.1',
    description='Custom theming for LMS',
    author='Curious Inc.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
