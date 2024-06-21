
from flask import Blueprint, render_template, jsonify
from flask_httpauth import HTTPBasicAuth

from config.config import BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD
from app.heater_control import turn_on_heater, turn_off_heater, get_heater_state

# Create a blueprint for the heater routes
bp = Blueprint('heater', __name__)

auth = HTTPBasicAuth()

@auth.verify_password
def authenticate(username, password):
    if username == BASIC_AUTH_USERNAME and password == BASIC_AUTH_PASSWORD:
        return True
    return False

@bp.route('/')
@auth.login_required
def index():
    return render_template('button.html')

@bp.route('/api/v1/heater/ping', methods=['GET'])
@auth.login_required
def get_ping():
    response = {'ping': 'pong'}
    return jsonify(response)

@bp.route('/api/v1/heater/state', methods=['GET'])
@auth.login_required
def get_state():
    state = get_heater_state()
    response = {'state': state}
    return jsonify(response)

@bp.route('/api/v1/heater/turn/<status>', methods=['PUT'])
@auth.login_required
def put_status(status):
    if status == 'on':
        turn_on_heater()
    elif status == 'off':
        turn_off_heater()

    state = get_heater_state()
    response = {'state': state}
    return jsonify(response)