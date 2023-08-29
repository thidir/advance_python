from gpiozero import Button
from signal import pause
import requests
from pushbutton import notnotify

event_name = "send an email"
api_key = "eJix5ABylAwAJ7HfDKCyEQ--nnToJR8wSdWaY-4OQrr"
json_data = {}

noti = notnotify(event_name,api_key,json_data)


def theFunc():
    return  noti.notify(json_data)


button1 = Button(2)
button1.when_pressed = theFunc
pause()