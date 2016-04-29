# -*- coding: utf-8 -*-

import re

import pytesseract
from PIL import Image


def get_songs_from_image(image):
    i = pytesseract.image_to_string(Image.open('example.jpg'))
    songs = re.findall('.*\s+[-—]\s+["].*?\n?.*"', i)
    songs = [s.replace('\n', ' ') for s in songs]
    return songs


if __name__ == '__main__':
    l = get_songs_from_image('example.jpg')
    print(l)
