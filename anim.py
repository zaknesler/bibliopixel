from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *
from BiblioPixelAnimations.strip import Searchlights

try:
    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=300, c_order='GRB', device_id=1)
    led = LEDStrip(driver)

    led.set_brightness(25)

    anim = Searchlights.Searchlights(led, 10, 0, 50)
    anim.run()
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
