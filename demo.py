from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *
# from BiblioPixelAnimations.strip import Rainbows

try:
    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=300, c_order='GRB', device_id=1)
    led = LEDStrip(driver)
    # anim = Rainbows.RainbowCycle(led)

    led.set_brightness(50)
    end = 300

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

    led.all_off()
    led.push_to_driver()
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
