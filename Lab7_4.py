import RPi.GPIO as GPIO

SW1 = 27 
SW2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, 
pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, 
pull_up_down=GPIO.PUD_UP)

import drivers
from time import sleep

display = drivers.Lcd()
display.lcd_clear()

try:
    while True:
        if GPIO.wait_for_edge(SW1, GPIO.FALLING):
            display.lcd_display_string("Charintorn",1)
            display.lcd_display_string("116510400232-4",2)
            display.lcd_display_string("Kritsanaphon",1)
            display.lcd_display_string("116510462003-4",2)
            sleep(0.3)
        elif GPIO.wait_for_edge(SW2, GPIO.FALLING):
            display.lcd_clear()
            display.lcd_display_string("bye")
            sleep(0.3)
            


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye...")