from robot import Robot
from time import sleep


def straight(bot, seconds):
    bot.set_left(80)
    bot.set_right(80)
    sleep(seconds)

def turn_left(bot, seconds):
    bot.set_left(20)
    bot.set_right(80)
    sleep(seconds)

def turn_right(bot, seconds):
    bot.set_left(80)
    bot.set_right(20)
    sleep(seconds)

def spin_left(bot, seconds):
    bot.set_left(-80)
    bot.set_right(80)
    sleep(seconds)


if __name__ == '__main__':
    bot = Robot()

    straight_time = 1
    turn_time = 0.6

    straight(bot, straight_time)
    turn_right(bot, turn_time)
    straight(bot, straight_time)
    turn_left(bot, turn_time)
    straight(bot, straight_time)
    turn_left(bot, turn_time)
    straight(bot, straight_time)
    spin_left(bot, turn_time)

