from machine import Pin ,PWM
from time import sleep
import utime

pir_pin = Pin(28, Pin.IN,Pin.PULL_DOWN)
led_pin = Pin (15, Pin.OUT)
buzzer = PWM(Pin(14))

while True:
    if pir_pin.value():
        print("Motion detected!")
        led_pin.value(1)
        buzzer.duty_u16(1000)
        buzzer.freq(4978)
        utime.sleep_ms(100)

    else :
        print("Motion not!")
        buzzer.duty_u16(0)    
    led_pin.value(0)