from flask import Flask, request
from shocker import Shocker

app = Flask(__name__)
channels = {
    1: Shocker(14),
    2: Shocker(15)
}


@app.route('/gpio/pulse/<channel>')
def pulse_action(channel):
    shocker = channels[channel]
    if shocker is None:
        return '{"error":"shocker not found"}'

    duration = request.args.get('duration')
    if duration is None:
        duration = 2

    shocker.pulse(duration)


if __name__ == '__main__':
    app.run()
