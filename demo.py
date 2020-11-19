from bibliopixel.drivers.serial.driver import *
from bibliopixel import LEDStrip

# import the module you'd like to use
from BiblioPixelAnimations.strip import Rainbows

# init driver with the type and count of LEDs you're using
driver = DriverSerial(ledtype=LEDTYPE.WS2812B, num=300, c_order='GRB', device_id=0)

# init controller
led = LEDStrip(driver)

# init animation; replace with whichever animation you'd like to use
# anim = Rainbows.RainbowCycle(led)

try:
    # run the animation
    # anim.run()

    for x in range(1, 300):
        led.setRGB(x, 255, 255, 0)

    for x in range(1, 255):
        led.set_brightness(x)
        time.sleep(0.01)
        led.push_to_driver()

    print("finish")
    led.all_off()
    led.push_to_driver()


except KeyboardInterrupt:
    # Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.push_to_driver()
