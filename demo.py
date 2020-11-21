import pygame
from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *

# import the module you'd like to use
# from BiblioPixelAnimations.strip import Rainbows

# init driver with the type and count of LEDs you're using
driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=300, c_order='GRB', device_id=1)

# init controller
led = LEDStrip(driver)

# init animation; replace with whichever animation you'd like to use
# anim = Rainbows.RainbowCycle(led)

try:
    # run the animation
    # anim.run()

    # while True:

    led.set_brightness(50)

    end = 30

    while True:
        for x in range(0, end):
            led.setRGB(x - 1, 0, 0, 0)
            led.setRGB(x, 255, 255, 0)
            led.push_to_driver()
            time.sleep(0.01)

        led.setRGB(end, 0, 0, 0)

        for x in range(end, 0, -1):
            led.setRGB(x + 1, 0, 0, 0)
            led.setRGB(x, 255, 255, 0)
            led.push_to_driver()
            time.sleep(0.01)

    input("Press the <ENTER> key to continue...")

    led.all_off()
    led.push_to_driver()


except KeyboardInterrupt:
    # Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.push_to_driver()
