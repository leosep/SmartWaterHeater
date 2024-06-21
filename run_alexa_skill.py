import os
from alexa_skill import return_skill
from common.gpio_controller import GPIOController
import RPi.GPIO as GPIO

app = return_skill()

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
current_working_dir = os.getcwd()

# Ensure the paths to the certificates are correct
cert_path = os.path.join(script_dir, 'certificates/certificate.pem')
key_path = os.path.join(script_dir, 'certificates/private-key.pem')

if __name__ == "__main__":
  try:
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=(cert_path, key_path))
  finally:
    GPIO.cleanup()