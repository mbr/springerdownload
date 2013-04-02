from setuptools import setup, find_packages

VERSION = "1.1"

setup(
    name='Springer Link Downloader',
    version=VERSION,
    description='Download whole books from link.springer.com',
    author='Thomas Vogt',
    author_email='tuxor1337@web.de',
    url='https://github.com/tuxor1337/springerdownload',
    packages=find_packages(),
    scripts=['springer_download.py'],
    install_requires=['pyPDF', 'beautifulsoup'],
    entry_points={
        'console_scripts': [
            'springerdl = springerdl.main:main',
        ],
    }
)
