from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit

motor_hat = Raspi_MotorHAT(addr=0x6f)
left_motor = motor_hat.getMotor(1)
right_motor = motor_hat.getMotor(2)


def turn_off_motors():
    left_motor.run(motor_hat.RELEASE)
    right_motor.run(motor_hat.RELEASE)


# atexit wil run the callback function when the program exits.
# This runs even if there is an error in the program!
atexit.register(turn_off_motors)

# Speed values range 0-255
left_motor.setSpeed(100)
right_motor.setSpeed(150)

left_motor.run(motor_hat.FORWARD)
right_motor.run(motor_hat.FORWARD)
time.sleep(1)

