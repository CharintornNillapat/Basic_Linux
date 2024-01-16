import RPi.GPIO as GPIO
import time

SW = 22
LED_RED = 18
LED_GREEN = 23
LED_BLUE = 24

RGB_LEDs = [LED_RED, LED_GREEN, LED_BLUE]

GPIO.setmode(GPIO.BCM)
GPIO.setup(RGB_LEDs, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_state = False
def toggle_led_state(led_pin, state):
    GPIO.output(led_pin, state)
    if state:
        print(f"LED {led_pin} ON")
    else:
        print(f"LED {led_pin} OFF")

def turn_off_all_leds():
    for led_pin in RGB_LEDs:
        toggle_led_state(led_pin, False)

def cycle_rgb_leds():
    colors = [
        (1, 0, 0),  
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0),  
        (1, 0, 1),  
        (0, 1, 1),  
        (1, 1, 1)   
    ]

    for color in colors:
        for i, led_pin in enumerate(RGB_LEDs):
            toggle_led_state(led_pin, color[i])
        time.sleep(1)

led_state = False 

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            led_state = not led_state
            cycle_rgb_leds()  
            turn_off_all_leds()
        else:
            time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye…")
