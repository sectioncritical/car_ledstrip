#!/usr/bin/env python3

import board
from busio import UART

import cmdparser

from adafruit_neopxl8 import NeoPxl8
from adafruit_led_animation.color import RED, GREEN, BLUE, WHITE

start_gpio = board.D2
num_strands = 2
pix_per_strand = 144
total_pix = num_strands * pix_per_strand
brightness=1
stride = 144
pulselen = 1

COLORON = (15, 0, 0)
COLOROFF = (0, 0, 0)

pxl8 = NeoPxl8(start_gpio, total_pix, num_strands=num_strands,
               brightness=brightness, auto_write=False)

uart = UART(tx=board.TX, rx=board.RX, baudrate=115200, timeout=0)

# take a string, append CRLF and send to uart
def uart_print(printstr):
    uart.write((printstr+"\r\n").encode("utf-8"))

# animation to turn everything off
def anim_off():
    for idx in range(total_pix):
        pxl8[idx] = COLOROFF
    pxl8.show()
    time.sleep(0.1)

def anim_help():
    uart_print("\nAnimation commands")
    uart_print("------------------")
    for key in anin_dict:
        uart_print(key)
    uart_print()

anim_dict = {
    "help": anim_help,
    "off": anim_off
    }

def run_animation():
    pass

# command format
# ascii string
# $cmdname,val\n
# command starts with '$'
# followed by command name as a string, such as IDLE, RPM, etc
# commands are case insensitive
# command name is followed by a comma, no spaces
# comma is followed by integer as string, no spaces
# if the command does not need a value, then use 0
# the command is terminated by a newline '\n'
# if any return chars appear '\r' they are discarded


errmsg = bytes("ERR\n", 'utf-8')
okmsg = bytes("OK\n", 'utf-8')

uart_print("\nFlashy Starting ...\n")

cp = cmdparser.CmdParser()

while True:
    in_available = uart.in_waiting
    if in_available:
        incoming = uart.read(in_available)
        uart.write(incoming)  # echo back to console
        cmdargs = cp.process_input(incoming)
        if cmdargs:
            if cmdargs[0] == "help":
                anim_help()
            else:
                uart.write(errmsg)

    run_animation()
