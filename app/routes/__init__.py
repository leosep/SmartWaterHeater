from flask import Blueprint

# Create a blueprint for the heater routes
bp = Blueprint('heater', __name__)

# Import the actual route handlers
from app.routes import heater