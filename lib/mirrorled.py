# Simple wrapper for the neopixel library to simplify first time coding for 9th grade engineering
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""Simple wrapper for the neopixel library for infinity mirror engineering project"""
import neopixel

class mirrorled():
    def __init__(self, pixel_pin, num_pixels=100, brightness=0.3, debug=False):
        """ Initialize the mirrorled class with the pin that the strip is connected to."""

        self._pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=True)
        self._debug = debug

    def on(self, address, color=(255,255,255)):
        self._pixels[address] = color

    def off(self, address):
        self._pixels[address] = (0, 0, 0)


