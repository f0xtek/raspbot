from Raspi_MotorHAT import Raspi_MotorHAT

import atexit


class Robot:
    def __init__(self, motorhat_addr=0x6f):
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)
        atexit.register(self.stop_motors)

    def convert_speed(self, speed):
        # choose the running mode
        mode = self._mh.RELEASE
        if speed > 0:
            mode = self._mh.FORWARD
        elif speed < 0:
            mode = self._mh.BACKWARD

        # scale the speed
        output_speed = (abs(speed) * 255) // 100
        return mode, int(output_speed)

    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)

    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)

    def stop_motors(self):
        self.left_motor.run(self._mh.RELEASE)
        self.right_motor.run(self._mh.RELEASE)
