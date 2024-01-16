import RPi.GPIO as GPIO
import time
SW = 22
LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = False 

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            led_state = not led_state 
            GPIO.output(LED, led_state)
            
            if led_state:
                print("LED ON")
            else:
                print("LED OFF")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye…")
