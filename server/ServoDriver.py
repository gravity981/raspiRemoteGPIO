import RPi.GPIO as GPIO


class ServoDriver:

    def __init__(self, servo_pin):
        self._servo_pin = servo_pin
        print("setup servo gpio with pin: " + str(servo_pin))
        GPIO.setup(self._servo_pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._servo_pin, 50)  # PWM with 50 Hz

    def start(self):
        self._pwm.start(0)
        self.off()

    def stop(self):
        self._pwm.stop()

    def set_and_hold_angle(self, angle: int):
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180
        duty_cycle = angle/18.0 + 2.5
        print("set servo on pin " + str(self._servo_pin) + " to angle: " + str(angle) + "° with dutycycle: " + str(duty_cycle))
        self._pwm.ChangeDutyCycle(duty_cycle)

    def off(self):
        # this unpowers the servo,
        # which makes it rotate freely only with friction from the gears
        print("power off servo on pin " + str(self._servo_pin))
        self._pwm.ChangeDutyCycle(0)
