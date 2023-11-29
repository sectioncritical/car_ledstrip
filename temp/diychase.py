# this is meant to run on adafruit RP2040 board
#
# Test program for bill bitners car project
# this is to run animation on 2 strings at the same time.
#
# Assumed hardware setup:
# * 2 neopixel strings
# * each is 144 pixels
# * attached to D2 and D3

import time
import board
from adafruit_neopxl8 import NeoPxl8
from adafruit_led_animation.color import RED, GREEN, BLUE, WHITE

start_gpio = board.D2
num_strands = 2
pix_per_strand = 144
total_pix = num_strands * pix_per_strand
brightness=1
stride = 144
pulselen = 1

pxl8 = NeoPxl8(start_gpio, total_pix, num_strands=num_strands,
               brightness=brightness, auto_write=False)

COLORON = (15, 0, 0)
COLOROFF = (0, 0, 0)

while True:
    for idx in range(pix_per_strand-1):
        pxl8[idx] = COLOROFF
        pxl8[idx+pix_per_strand] = COLOROFF
        pxl8[idx+1] = COLORON
        pxl8[idx+1+pix_per_strand] = COLORON
        pxl8.show()

"""
while True:
    for startidx in range(stride):
        for idx in range(startidx):
            col = COLOROFF if (startidx - idx) < (stride - pulselen) else COLORON
            pxl8[idx] = col
            pxl8[idx+pix_per_strand] = col
        for idx in range(startidx, startidx+pulselen):
            for jdx in range(idx, pix_per_strand, stride):
                pxl8[jdx] = COLORON
                pxl8[jdx+pix_per_strand] = COLORON
        for idx in range(startidx+pulselen, startidx+stride):
            for jdx in range(idx, pix_per_strand, stride):
                pxl8[jdx] = COLOROFF
                pxl8[jdx+pix_per_strand] = COLOROFF
        pxl8.show()
#        time.sleep(0.005)
"""
"""
stride = 10
pulselen = 3

for _ in range(2):
    for startidx in range(stride):
        for idx in range(startidx):
            pxl8[idx] = 0 if (startidx - idx) < (stride - pulselen) else 1
        for idx in range(startidx, startidx+pulselen):
            for jdx in range(idx, 40, stride):
                pxl8[jdx] = 1
        for idx in range(startidx+pulselen, startidx+stride):
            for jdx in range(idx, 40, stride):
                pxl8[jdx] = 0
        print(pxl8)
"""
