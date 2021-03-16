"""
My OCR.
~~~~~~~~~~~~~~~~~~~~~

Python package for My OCR

Basic usage:
    >>> import my_ocr
    >>> my_ocr()

To see language support in pytesseract
    >>> print(pytesseract.get_languages(config=''))

:copyright: (c) 2021 Parag M.
:license: MIT, see LICENSE for more details.
"""
from os import environ, path
import logging

import re
from PIL import Image
import numpy as np
import pytesseract
from pytesseract import Output
from matplotlib import pyplot as plt

ENVIRONMENT = environ.get('ENVIRONMENT', 'development')
SETTINGS = dict()

logger = logging.getLogger(ENVIRONMENT)
logger.setLevel(logging.DEBUG)

here = path.abspath(path.dirname(__file__))
IMG_DIR = path.join(here, 'images')
OUTPUT_DIR = path.join(here, 'outputs')

# -------- Tesseract variables
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# -------- Methods
# get grayscale image
def get_grayscale(img):
    print("TODO")
    return img

def write_searchable_pdf(img):
    """Convert image to a searchable pdf
    """
    opdf = path.join(OUTPUT_DIR, 'output.pdf')
    pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
    with open(opdf, 'w+b') as f:
        f.write(pdf) # pdf type is bytes by default


def get_table_string(img):
    """Print string entries from a tabular image such as spreadsheet images
    """
    custom_config = r'-l eng --oem 3 --psm 6'
    output: str = pytesseract.image_to_string(img, config=custom_config)
    return output


def get_words(img):
    cfg_filename = 'words'
    output: str = pytesseract.run_and_get_output(img, extension='txt', config=cfg_filename)
    return output


# --------- Main
def main(*args, **kwargs):
    """Do some processing

    :some_arg type: describe the argument `some_arg`
    """

    # Read image
    img = Image.open(path.join(IMG_DIR, 'read-tomatocsv.png'))

    # run some processing
    print(get_table_string(img))


# ==============================
if __name__ == '__main__':
    main()
