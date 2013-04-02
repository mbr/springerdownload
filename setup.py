import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='springerdl',
    version='1.2-dev',
    description='Download whole books from link.springer.com',
    author='Marc Brinkmann <git@marcbrinkmann.de>, '
           'Thomas Vogt <tuxor1337@web.de>',
    author_email='git@marcbrinkmann.de',
    url='https://github.com/tuxor1337/springerdownload',
    packages=find_packages(),
    install_requires=['pyPDF', 'beautifulsoup', 'requests'],
    entry_points={
        'console_scripts': [
            'springerdl = springerdl.main:main',
        ],
    }
)
