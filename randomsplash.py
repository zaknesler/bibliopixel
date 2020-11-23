import random
from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *

try:
    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=92, c_order='GRB', device_id=1)
    led = LEDStrip(driver)
    led.set_brightness(255)

    distance = 20
    delay = 0.01

    while True:
        index = random.randint(0, driver.numLEDs)

        # Light main LED
        led.all_off()
        led.setHSV(index, (255, 255, 255))
        led.push_to_driver()

        for i in range(0, distance + 1):
            hue = round(255 - ((i * 255) / distance))

            # Light next LEDs
            led.setHSV(index - i, (hue, 255, 255))
            led.setHSV(index + i, (hue, 255, 255))

            # Turn off previously-lit LEDs
            led.setRGB(index - i + 1, 0, 0, 0)
            led.setRGB(index + i - 1, 0, 0, 0)

            led.push_to_driver()
            time.sleep(delay)

        led.all_off()
        led.push_to_driver()
        time.sleep(delay * (distance + 1))
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
