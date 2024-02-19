import RPi.GPIO as GPIO
import time
"""
    Breadboard Setup:
        Channel 1 (3v3) to Capacitor A
        Capacitor A to Book Switch
        Book Switch to Line to Channel 10 (RXD UART)
        Channel 7 (GPIO 4) to Capacitor B
        Capacitor B to Light to Ground
"""

BTN_BOOK_INPUT_CHANNEL = 10
DOOR_SIGNAL_CHANNEL = 7


def button_callback(channel):
    button_callback.counter += 1
    print("Button Pushed ",  str(button_callback.counter))
    if(GPIO.input(BTN_BOOK_INPUT_CHANNEL)):
        print("Book signal ON - Do Nothing")
    else:
        print("Book signal OFF - Open Door")            
        GPIO.output(DOOR_SIGNAL_CHANNEL, False)
        time.sleep(2)
        GPIO.output(DOOR_SIGNAL_CHANNEL, True)
    
button_callback.counter = 0
print("Starting up....")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print("Turning on door signal. Ensure button depressed")
GPIO.setup(DOOR_SIGNAL_CHANNEL, GPIO.OUT)
time.sleep(1)
print("Reading door signal")
#GPIO.setup(BTN_BOOK_INPUT_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_BOOK_INPUT_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("Door signal event feed live")
#Setup event callback for when button is pressed
#GPIO.add_event_detect(BTN_BOOK_INPUT_CHANNEL, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(BTN_BOOK_INPUT_CHANNEL, GPIO.BOTH, callback=button_callback, bouncetime=200)
#Turn on power to door lock to start
GPIO.output(DOOR_SIGNAL_CHANNEL, True)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
