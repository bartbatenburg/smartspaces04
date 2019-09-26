from flask import Flask, request
from shocker import Shocker

app = Flask(__name__)
channels = {
    '1': Shocker(14),
    '2': Shocker(15)
}


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
