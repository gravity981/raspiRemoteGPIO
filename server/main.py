import json
import sys
import RPi.GPIO as GPIO
from server.GpioDeviceController import GpioDeviceController
from server.GpioHttpServer import GpioHttpServer


def read_config() -> dict:
    # read file
    with open('config.json', 'r') as configFile:
        data = configFile.read()

    # parse file
    config = json.loads(data)
    return config


def check_config(config: dict) -> bool:
    if 'server' not in config:
        return False
    if 'device' not in config:
        return False
    if 'port' not in config['server']:
        return False
    if not type(config['server']['port']) is int:
        return False
    if not type(config['device']) is list:
        return False
    return True


def main():
    config = read_config()
    if not check_config(config):
        print('invalid configuration')
        sys.exit(1)
    print('config loaded')

    # init general stuff
    GPIO.setmode(GPIO.BCM)  # pin numbering mode

    # init devices
    device_controller = GpioDeviceController(config['device'])
    device_controller.init_devices()

    # init http server
    server = GpioHttpServer(config['server']['port'], device_controller)

    # run
    try:
        device_controller.start_devices()
        server.start()
    except KeyboardInterrupt:
        print("stop application")

    # stop app
    device_controller.stop_devices()

    # de-init general stuff
    GPIO.cleanup()  # cleanup any changes made to gpios





main()
