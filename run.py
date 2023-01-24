#!/usr/bin/env python3
import sys
# try:
from PIL import Image
# from datetime import date
import datetime

import time
timestr = time.strftime("%d%m%Y-%H%M%S")


def add_logo():
    mimage = Image.open('/baseimage.jpg')
    limage = Image.open("1-bg.png")
    today = timestr
    mimage.paste(limage, (0, 0), limage)
    mimage.save("new/"+today+".jpg")

    mimage = Image.open('/baseimage.jpg')
    limage = Image.open("2-bg.png")
    mimage.paste(limage, (0, 0), limage)
    mimage.save("2/"+today+".jpg")

add_logo()