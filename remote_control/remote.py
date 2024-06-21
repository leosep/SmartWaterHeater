import time
from common.gpio_controller import GPIOController
import RPi.GPIO as GPIO
from app.heater_control import turn_on_heater, turn_off_heater, get_heater_state

# Constants
HEATER_GPIO_PIN = 17

gpio_controller = GPIOController(HEATER_GPIO_PIN)

def run_remote_control():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        inputValue = GPIO.input(18)
        if not inputValue:
            if get_heater_state() == GPIO.HIGH:
                turn_off_heater()
            else:
                turn_on_heater()
            time.sleep(0.5)
        time.sleep(0.3)