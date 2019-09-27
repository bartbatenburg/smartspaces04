from flask import Flask, request
from sensor import Sensor
from shocker import Shocker
from threading import Thread
from time import sleep

app = Flask(__name__)
channels = {
    '1': Shocker(14),
    '2': Shocker(15)
}
sensors = [
    Sensor(0, 0x68),
    Sensor(1, 0x68)
]


@app.route('/gpio/<channel>/pulse')
def pulse_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    duration = request.args.get('duration')
    if duration is None:
        duration = 2
    else:
        duration = float(duration)

    shocker.async_pulse(duration)
    return '{"status":"okay"}'


@app.route('/gpio/<channel>/on')
def on_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    shocker.on()
    return '{"status":"okay"}'


@app.route('/gpio/<channel>/off')
def off_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    shocker.off()
    return '{"status":"okay"}'


@app.route('/gpio/<channel>')
def status_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    return '{"status":%s}' % ("true" if shocker.state else "false")


def check_loop():
    while True:
        sensors[0].update()
        sensors[1].update()

        x2 = abs(sensors[1].x)
        z2 = abs(sensors[1].z)

        if ((x2 > 0.5 and z2 > 0.7) or (z2 > 0.5 and x2 > 0.7)) and sensors[0].x > 0.4:
            print("SHOCK")
        else:
            print("NO SHOCK (X1=%f, Z1=%f, X2=%f, Z2=%f)" % (
                sensors[0].x, sensors[0].z, sensors[1].x, sensors[1].z))

        sleep(0.5)


Thread(target=check_loop).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
