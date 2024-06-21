import os
from crontab import CronTab
from datetime import datetime, timedelta

from config.config import HEATER_GPIO_PIN, HEATER_MINUTES_TIMER, LINUX_USERNAME
from common.gpio_controller import GPIOController

gpio_controller = GPIOController(HEATER_GPIO_PIN)

def schedule_turn_off():
    my_cron = CronTab(user=LINUX_USERNAME)
    current_time = datetime.now()
    future_time = current_time + timedelta(minutes=HEATER_MINUTES_TIMER)
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    turn_off_script_file = os.path.join(script_dir, '../scripts/turn_off_script.py')
    job = my_cron.new(command='python3 ' + turn_off_script_file, comment='turnoff')

    job.hour.on(future_time.hour)
    job.minute.on(future_time.minute)

    my_cron.write()

def cancel_turn_off():
    my_cron = CronTab(user=LINUX_USERNAME)
    for job in my_cron:
        if job.comment == 'turnoff':
            my_cron.remove(job)
            my_cron.write()

def turn_on_heater():
    gpio_controller.turn_on()
    schedule_turn_off()

def turn_off_heater():
    gpio_controller.turn_off()
    cancel_turn_off()

def get_heater_state():
    return gpio_controller.get_state()