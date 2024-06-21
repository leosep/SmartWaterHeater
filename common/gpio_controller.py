import RPi.GPIO as GPIO

class GPIOController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def get_state(self):
        return GPIO.input(self.pin)

    def cleanup(self):
        GPIO.cleanup()
