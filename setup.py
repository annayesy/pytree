# setup.py
from setuptools import setup, find_packages

setup(
    name='pytreelib',
    version='1.0',
    packages=find_packages(where='pytreelib'),
    package_dir={'':'pytreelib'},
    license="MIT",
    author="Anna Yesypenko",
    author_email='annayesy@utexas.edu',
    url='https://github.com/annayesy/pytree',
    install_requires=[
        'numpy',
    ],
)