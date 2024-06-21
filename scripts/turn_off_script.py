import sys
import os

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the script directory
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

# Print sys.path for debugging
print("sys.path:", sys.path)

from app.heater_control import turn_off_heater

turn_off_heater()