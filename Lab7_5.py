import RPi.GPIO as GPIO
L = "Lab7"
text = list(L)

SW1 = 27 
SW2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, 
pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, 
pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
lcd_position = 0

import drivers
from time import sleep

display = drivers.Lcd()


try:
    while True:
        if GPIO.event_detected(SW1) and len(text) < 16 :
            display.lcd_clear()
            text.insert(0," ")
            
        elif GPIO.event_detected(SW2) and len(text) > 4 :

            display.lcd_clear()
            text.pop(0)
        
        display.lcd_display_string(text ,1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye...")