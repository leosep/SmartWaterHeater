def create_skill():
    import os
    from flask import Flask
    from flask_ask import Ask, statement

    from app.heater_control import turn_on_heater, turn_off_heater
    from config.config import HEATER_MINUTES_TIMER

    app = Flask(__name__)
    ask = Ask(app, '/')

    @ask.intent('HeaterIntent', mapping={'status': 'status'})
    def heater(status):
        if status == 'on':
            turn_on_heater()
            time_text = 'for {} minutes'.format(HEATER_MINUTES_TIMER)
            return statement('Turning the water heater on {}'.format(time_text))
        elif status == 'off':
            turn_off_heater()
            return statement('Turning the water heater off')
    
    return app