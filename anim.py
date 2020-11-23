from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *
from BiblioPixelAnimations.strip import LarsonScanners

try:
    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=186, c_order='GRB', device_id=1)
    led = LEDStrip(driver)

    led.set_brightness(255)

    anim = LarsonScanners.LarsonScanner(led, 10)
    anim.run()
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
