from app import sensors, channels
from time import sleep

run_detection = True


def halt():
    global run_detection
    run_detection = False


def resume():
    global run_detection
    run_detection = True


def status():
    global run_detection
    return run_detection


def detection_loop():
    while True:
        if run_detection:
            sensors[0].update()
            sensors[1].update()

            x2 = abs(sensors[1].x)
            z2 = abs(sensors[1].z)

            if ((x2 > 0.5 and z2 > 0.7) or (z2 > 0.5 and x2 > 0.7)) and sensors[0].x > 0.4:
                channels['1'].on()
                channels['2'].on()
            else:
                channels['1'].off()
                channels['2'].off()

        sleep(0.1)


if __name__ == '__main__':
    detection_loop()
