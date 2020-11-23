import pygame
from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *

try:
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    clock = pygame.time.Clock()

    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=300, c_order='GRB', device_id=1)
    led = LEDStrip(driver)
    led.set_brightness(50)

    font = pygame.font.SysFont(None, 24)
    image = font.render('Focus this window and begin typing...', True, pygame.Color('white'))
    screen.blit(image, (20, 20))
    pygame.display.update()

    while True:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                led.all_off()
                led.push_to_driver()
                quit()
            elif event.type == pygame.KEYDOWN:
                index = event.key - 97
                distance = 15
                delay = 0.001

                # Light main LED
                led.all_off()
                led.setHSV(index, (255, 255, 255))
                led.push_to_driver()

                for i in range(1, distance + 1):
                    hue = 255 - i * 10

                    # Light next LED
                    led.setHSV(index - i, (hue, 255, 255))
                    led.setHSV(index + i, (hue, 255, 255))

                    # Turn off previously-lit LEDs
                    led.setRGB(index - i + 1, 0, 0, 0)
                    led.setRGB(index + i - 1, 0, 0, 0)

                    led.push_to_driver()
                    time.sleep(delay)

                led.all_off()
                led.push_to_driver()

    led.all_off()
    led.push_to_driver()
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
