from flask import Flask, request
from flask_cors import CORS, cross_origin

from detection import detection_loop, status, halt, resume
from sensor import Sensor
from shocker import Shocker
from threading import Thread

app = Flask(
    __name__,
    static_url_path='', static_folder='static/'
)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

channels = {
    '1': Shocker(14),
    '2': Shocker(15)
}
sensors = [
    Sensor(0, 0x68),
    Sensor(1, 0x68)
]
run_detection = True


@app.route('/gpio/<channel>/pulse')
@cross_origin()
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
@cross_origin()
def on_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    shocker.on()
    return '{"status":"okay"}'


@app.route('/gpio/<channel>/off')
@cross_origin()
def off_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    shocker.off()
    return '{"status":"okay"}'


@app.route('/gpio/<channel>')
@cross_origin()
def status_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    return '{"status":%s}' % ("true" if shocker.state else "false")


@app.route('/detection/on')
@cross_origin()
def detection_on_action():
    resume()
    return '{"status":"okay"}'


@app.route('/detection/off')
@cross_origin()
def detection_off_action():
    halt()
    return '{"status":"okay"}'


@app.route('/detection')
@cross_origin()
def detection_status_action():
    return '{"status":%s}' % ("true" if status() else "false")


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', port=80
    )
    Thread(target=detection_loop).start()
