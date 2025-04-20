from machine import Pin
import time

led = Pin(25, Pin.OUT)  # Interne LED vom Pico

def blink(duration):
    led.on()
    time.sleep(duration)
    led.off()
    time.sleep(0.3)

while True:
    # Rhythmus: kurz–kurz–lang
    blink(0.2)  # kurz
    blink(0.2)  # kurz
    blink(0.6)  # lang
    time.sleep(1.5)  # Pause bis zum nächsten Zyklus
