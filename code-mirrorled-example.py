# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from mirrorled import mirrorled

# ** Change this value to connnect the DIN wire to a different pin on the Pico
pixel_pin = board.GP2
# ** Change this value to be the number of pixels on your strip
num_pixels = 10

# This line initialized the library used to control the neopixel strip
mirrorled = mirrorled(pixel_pin, num_pixels)

# Different colors are made by mixing different amounts of
# Red, Green and Blue light.  The color wheel for light
# is different from mixing paint!
#
# Here are some RGB values for some common colors.
# 0 == LED off and 255 == full brightness
RED    = (255,   0,   0) # 100% red,   0% green, 0% blue
GREEN  = (  0, 255,   0) #   0% red, 100% green, 0% blue
BLUE   = (  0,   0, 255) # 100% blue
CYAN   = (  0, 255, 255) #   0% red, 100% green, 100% blue
YELLOW = (255, 150,   0) # 100% red,  55% green, 0% blue
WHITE  = (100, 100, 100) # 100% of all colors
BLACK  = (  0,   0,   0) # 0% of all colors (turns the LED off)

# ** Can you figure out the values for these colors?
#LIGHTBLUE = (?, ?, ?)
#LIGHTPINK = (?, ?, ?)
#ORANGE = (?, ?, ?)
#CYAN = (?, ?, ?)
#PURPLE = (?, ?, ?)
#MAGENTA = (?, ?, ?)

# ** Make your own colors and see what happens!
#MYCOLOR1 RGB(?, ?, ?)
#MYCOLOR2 RGB(?, ?, ?)
#MYCOLOR3 RGB(?, ?, ?)
#MYCOLOR4 RGB(?, ?, ?)

# *****************************************************************************
# ** These are the functions used to make different patterns.
# ** Skip down to "while True:" below to start making your changes to the code
# *****************************************************************************
def color_chase(color, wait):
    for address in range(num_pixels):
        mirrorled.on(address, color)
        time.sleep(wait)


# theater_chase(color, wait)
# Theatre-style crawling lights.
#  color - The color to use for the LEDs
#  wait - The number of seconds to wait between turning the LEDs on and off.
def theater_chase(color, wait):
    if num_pixels > 1:
        mirrorled.off(num_pixels - 1)
    if num_pixels > 2:
        mirrorled.off(num_pixels - 2)
    for j in range(10): #do 10 cycles of chasing
        for q in range(3):
            for i in range(0, num_pixels-1, 3):
                mirrorled.on(i+q,color) # turn every third pixel on
            time.sleep(wait);
            for i in range(0, num_pixels-1, 3):
                mirrorled.off(i+q)#  turn every third pixel off


##############################################################################
# This is the main body of your code
while True:

    # Clear out the pixel strip
    for address in range(num_pixels):
        mirrorled.off(address)

    # ** You can make changes below here

    # print() shows a message in the Serial Monitor.
    # Open it using the "Serial" icon at the top of the Mu Editor
    print("Showing colors");

    # Setting pixel[N] to a color sets one pixel at position N to a specific color
    # Note that the first pixel starts at zero!

    # Set the first 5 pixels to a specific color
    mirrorled.on(0, RED)
    mirrorled.on(1, BLUE)
    mirrorled.on(2, GREEN)
    mirrorled.on(3, BLACK)
    mirrorled.on(4, WHITE)

    # time.sleep() pauses the program for the specified number of seconds.
    # You can use a decimal to pause for less than a second, e.g. time.sleep(.5)
    time.sleep(4)

    # pixels.fill() sets every LED to the same color
    print ("Turning off all LEDs on the strip");
    for address in range(num_pixels):
        mirrorled.off(address)
    time.sleep(2)

    print("color_chase(BLUE): moves red across the strip")
    color_chase(BLUE, 0.1)  # Increase the number to slow down the color chase

    print("theater_chase(): make lights run up the strip")
    theater_chase(RED, .1)
