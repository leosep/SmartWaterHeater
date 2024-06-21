# SmartWaterHeater Project 

Basically this source code is for a DIY smart plug. This project implements a Smart Heater Service using Flask, Raspberry Pi GPIO control, and cron scheduling. The service allows turning a heater on and off based on user commands via an Alexa skill and provides a web API for remote control.

## Functionality

- **Flask Web API**: Provides endpoints for turning the heater on/off and checking its state.
- **Alexa Skill Integration**: Controls the heater via an Alexa skill using Flask-Ask.
- **GPIO Control**: Uses RPi.GPIO to control the GPIO pin of the heater.
- **Cron Scheduling**: Uses `python-crontab` to schedule turning off the heater after a specified time.
- **Basic Authentication**: Protects API endpoints with HTTP Basic Authentication.
