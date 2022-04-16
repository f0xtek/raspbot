from robot import Robot
from time import sleep


def straight(bot, seconds):
    bot.set_left(50)
    bot.set_right(50)
    sleep(seconds)

def turn_left(bot, seconds):
    bot.set_left(5)
    bot.set_right(50)
    sleep(seconds)

def turn_right(bot, seconds):
    bot.set_left(50)
    bot.set_right(5)
    sleep(seconds)

def spin_left(bot, seconds):
    bot.set_left(-50)
    bot.set_right(50)
    sleep(seconds)


if __name__ == '__main__':
    bot = Robot()

    straight_time = 1
    turn_time = 0.9

    straight(bot, straight_time)
    turn_right(bot, turn_time)
    straight(bot, straight_time)
    turn_left(bot, turn_time)
    straight(bot, straight_time)
    turn_left(bot, turn_time)
    straight(bot, straight_time)
    spin_left(bot, turn_time)

