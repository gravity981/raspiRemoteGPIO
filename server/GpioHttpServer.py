from http.server import BaseHTTPRequestHandler,HTTPServer
from server.GpioDeviceController import GpioDeviceController


class GpioHttpServer:
    _server = None

    def __init__(self, port, device_controller: GpioDeviceController):
        MyHandler.device_controller = device_controller
        self._server = HTTPServer(('', port), MyHandler)

    def start(self):
        self._server.serve_forever()


class MyHandler(BaseHTTPRequestHandler):
    device_controller = None

    @staticmethod
    def handle_servo_request(tokens) -> bool:
        # index and angle expected
        if len(tokens) != 2:
            return False  # wrong number of tokens
        if MyHandler.device_controller is None:
            return False  # handler not setup correctly
        servo_list = MyHandler.device_controller.get_servos()
        servo_index = None
        try:
            servo_index = int(tokens.pop(0))
        except ValueError:
            return False  # index not a number
        if servo_index < 0 or servo_index >= len(servo_list):
            return False  # index out of bounds
        angle = None
        raw_value = tokens.pop(0)
        # special case to turn off servo
        if raw_value == 'off':
            servo_list[servo_index].off()
            return True
        # set the servo angle
        try:
            angle = int(raw_value)
        except ValueError:
            return False  # angle not a number
        servo_list[servo_index].set_and_hold_angle(angle)
        return True

    def do_GET(self):
        tokens = self.path.split('/')
        tokens.pop(0)  # not interested in root '/'
        if len(tokens) == 0:
            self.send_response(400)
            return
        device_type = tokens.pop(0)
        if device_type == 'servo':
            if MyHandler.handle_servo_request(tokens):
                self.send_response(200)
            else:
                self.send_response(400)
            return
        self.send_response(400)
