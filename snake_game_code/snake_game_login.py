from snake_game import *
import time, msvcrt, os


snack = []
fruit = [('a', 'a')]
direction = 'w'
snack_init(snack)


if __name__ == "__main__":

    juge = game_go(snack, direction, fruit)
    if juge == 0 or juge == 1:
        exit()






