import datetime

from device import Device
# from flask import Application
from flask import Flask
from CONSTANTS import *

app = Flask(__name__)
app.config['SECRET_KEY'] = TOKEN
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)


def connect_devices():
    devices = [Device("convector1", 0, False),
               Device("convector2", 1, False),
               Device("convector3", 2, False)]
    return devices


devices = connect_devices()


@app.route('/all_devices')
def all_devices():
    res = {}
    for device in devices:
        res.update(device.to_json())
    return res
