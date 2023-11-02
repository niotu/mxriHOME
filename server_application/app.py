import datetime

from convector import Convector
# from flask import Application
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)


def connect_devices():
    devices = [Convector("convector1", 0, False),
               Convector("convector2", 1, False),
               Convector("convector3", 2, False)]
    return devices


devices = connect_devices()


@app.route('/all_devices')
def all_devices():
    res = {}
    for device in devices:
        res.update(device.to_json())
    return res
