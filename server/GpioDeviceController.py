from ServoDriver import ServoDriver


class GpioDeviceController:

    def __init__(self, devices_config):
        self._devices_config = devices_config
        self._devices = dict()

    def init_devices(self):
        for device_config in self._devices_config:
            if device_config['type'] == 'servo':
                if 'servo' not in self._devices:
                    self._devices['servo'] = list()
                servo = ServoDriver(device_config['gpio'])
                self._devices['servo'].append(servo)
            else:
                print("warning: unsupported device type: " + device_config['type'])

    def start_devices(self):
        for servo in self._devices['servo']:
            servo.start()

    def stop_devices(self):
        for servo in self._devices['servo']:
            servo.stop()

    def get_servos(self) -> dict:
        return self._devices['servo']
