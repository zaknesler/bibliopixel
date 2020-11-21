import pygame
from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *

try:
    pygame.init()
    screen = pygame.display.set_mode((720, 480))
    clock = pygame.time.Clock()

    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=300, c_order='GRB', device_id=1)
    led = LEDStrip(driver)
    led.set_brightness(50)

    while True:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                led.all_off()
                led.push_to_driver()
                quit()
            elif event.type == pygame.KEYDOWN:
                led.all_off()
                led.setRGB(event.key - 97, 255, 255, 0)
                led.push_to_driver()

    led.all_off()
    led.push_to_driver()
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
