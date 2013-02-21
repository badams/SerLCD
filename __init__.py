'''
    SerLCD

    A Simple Wrapper Class for the SparkFun SerLCD ver 2.5
    This was developed and tested on a RaspberryPi Board, using
    a debian based distro, Though should work on other machines 
    and distributions.
    
    More information about the Sparkfun SerLCD board can be found here:
    http://www.sparkfun.com/datasheets/LCD/SerLCD_V2_5.PDF

    Copyright (C) 2013 Byron Adams <byron.adams54@gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a 
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation 
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the 
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included 
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
    THE SOFTWARE.

'''

from serial import Serial
from time import sleep

class SerLCD:

    COMMAND      = 0xFE
    SPECIAL_CMD  = 0x7C
    CLEAR        = 0x01
    NEWLINE      = 0xC0
    SETSPLASH    = 0x0A
    TOGGLESPLASH = 0x09

    BACKLIGHT = {
        'OFF'    : 0x80,
        'LOW'    : 0x8C,
        'MEDIUM' : 0x96,
        'FULL'   : 0x9D
    }

    DISPLAY = {
        'ON'  : 0x0C,
        'OFF' : 0x08
    }

    def __init__(self, port='/dev/ttyAMA0', baudrate=9600):
        self.ser = Serial(port, baudrate)
        self.ser.open()

    def cmd(self, bits):        
        self.ser.write(chr(self.COMMAND) + chr(bits))
    
    def scmd(self, bits):
        self.ser.write(chr(self.SPECIAL_CMD) + chr(bits))

    def Backlight(self, val):
        try:
            self.scmd(self.BACKLIGHT[val])
        except (KeyError):
            raise Exception('Invalid backlight value! use: OFF, LOW, MEDIUM or FULL')

    def Clear(self):
        self.cmd(self.CLEAR)

    def NewLine(self):
        self.cmd(self.NEWLINE)

    def Display(self, val):
        self.scmd(self.DISPLAY[val])
    
    def ToggleSplash(self):
        self.scmd(self.TOGGLESPLASH)

    def SetSplash(self):
        self.scmd(self.SETSPLASH)        

    def Text(self, str, delay = 0):
        for s in str:
            self.ser.write(s)
            sleep(delay)

