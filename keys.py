import pygame
from bibliopixel import LEDStrip
from bibliopixel.drivers.serial.driver import *

try:
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    clock = pygame.time.Clock()

    driver = DriverSerial(ledtype=LEDTYPE.NEOPIXEL, num=92, c_order='GRB', device_id=1)
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
                led.all_off()
                led.setRGB(event.key - 97, 255, 255, 0)
                led.push_to_driver()

    led.all_off()
    led.push_to_driver()
except KeyboardInterrupt:
    led.all_off()
    led.push_to_driver()
