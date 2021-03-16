"""Setuptools package file for My OCR."""
import io
from os import environ, path
from setuptools import setup, find_packages

AUTHOR = environ.get('AUTHOR', 'Parag M')
AUTHOR_EMAIL = environ.get('AUTHOR_EMAIL', 'admin@bitsofparag.com')
PACKAGE_VERSION = environ.get('PACKAGE_VERSION', '0.1.0')

here = path.abspath(path.dirname(__file__))
readme = io.open(path.join(here, 'README'), 'r', encoding='utf-8').read()
requirements = io.open(path.join(here, 'requirements.txt'), 'r').read().splitlines()


setup(
    name='my_ocr',
    version=PACKAGE_VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license='MIT',
    description='''
    Python package for My OCR
    ''',
    long_description=readme,
    url='https://github.com/bitsofparag/my_ocr.git',
    packages=find_packages(exclude=['test*']),
    python_requires='!=2.*, >3.0, >=3.8.6',
    setup_requires=['wheel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'my_ocr = my_ocr.main:main',
        ],
    },
)
