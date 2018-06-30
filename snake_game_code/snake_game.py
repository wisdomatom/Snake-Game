from multiprocessing import Process
import time, random
import msvcrt, os

map_size = [0, 10]
speed = 0.5

def map_print(snack, fruit, direction):

    # print('-'*(22))
    for i in range(map_size[1]):
        # print('|', end='')
        for j in range(map_size[1]):
            if (i, j) in snack:
                if (direction == 'w') and ((i,j) == snack[0]):
                    print('▲', end='')
                elif (direction == 's') and ((i,j) == snack[0]):
                    print('▼', end='')
                elif (direction == 'a') and ((i,j) == snack[0]):
                    print('◀', end='')
                elif (direction == 'd') and ((i,j) == snack[0]):
                    print('▶', end='')
                else:
                    print('OO', end='')
            elif (i, j) == fruit[0]:
                print('♥', end='')
            else:
                print('--', end='')
        print('')
    print('+'*(46))

def snack_up(snack, fruit):
    if (snack[0][0] - 1, snack[0][1]) in snack:
        return 2
    elif (snack[0][0] - 1, snack[0][1]) == (fruit[0]):
        snack.insert(0, (snack[0][0] - 1, snack[0][1]))
        fruit[0] = ('a', 'a')
    else:
        snack.insert(0, (snack[0][0] - 1, snack[0][1]))
        snack.pop()
def snack_down(snack, fruit):
    if (snack[0][0] + 1, snack[0][1]) in snack:
        return 2
    elif (snack[0][0] + 1, snack[0][1]) == (fruit[0]):
        snack.insert(0, (snack[0][0] + 1, snack[0][1]))
        fruit[0] = ('a', 'a')
    else:
        snack.insert(0, (snack[0][0] + 1, snack[0][1]))
        snack.pop()
def snack_left(snack, fruit):
    if (snack[0][0], snack[0][1] - 1) in snack:
        return 2
    elif (snack[0][0], snack[0][1] - 1) == (fruit[0]):
        snack.insert(0, (snack[0][0], snack[0][1] - 1))
        fruit[0] = ('a', 'a')
    else:
        snack.insert(0, (snack[0][0], snack[0][1] - 1))
        snack.pop()
def snack_right(snack, fruit):
    if (snack[0][0], snack[0][1] + 1) in snack:
        return 2
    elif (snack[0][0], snack[0][1] + 1) == (fruit[0]):
        snack.insert(0, (snack[0][0], snack[0][1] + 1))
        fruit[0] = ('a', 'a')
    else:
        snack.insert(0, (snack[0][0], snack[0][1] + 1))
        snack.pop()

def snack_state(snack):
    if not snack[1]:
        return 1
    elif snack[0][0] + 1 == snack[1][0]:
        return 2 #不能往下移
    elif snack[0][1] - 1 == snack[1][1]:
        return 3 #不能往左移
    elif snack[0][0] - 1 == snack[1][0]:
        return 4 #不能往上移
    elif snack[0][1] + 1 == snack[1][1]:
        return 5 #不能往右移

def snack_move(snack, direction, fruit):
    state = snack_state(snack)

    if direction not in ['w', 's', 'a', 'd']:
        return 0
    elif (direction == 'w') and (snack[0][0] == map_size[0]):
        return 1
    elif (direction == 's') and (snack[0][0] == (map_size[1] - 1)):
        return 1
    elif (direction == 'a') and (snack[0][1] == map_size[0]):
        return 1
    elif (direction == 'd') and (snack[0][1] == (map_size[1] - 1)):
        return 1
    elif (direction == 'w') and (state != 4):
        return snack_up(snack, fruit)
    elif (direction == 's') and (state != 2):
        return snack_down(snack, fruit)
    elif (direction == 'a') and (state != 3):
        return snack_left(snack, fruit)
    elif (direction == 'd') and (state != 5):
        return snack_right(snack, fruit)

def snack_init(snack):

    (x, y) = (map_size[1]/2, map_size[1]/2)
    a = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    (x2, y2) = (x + 1), y
    snack.append((x, y))
    snack.append((x2, y2))
    # direction = 'w'


def food(snake, fruit):

    if fruit[0] == ('a', 'a'):
        map_set = {(x, y) for x in range(map_size[0], map_size[1]) for y in range(map_size[0], map_size[1])}
        snake_set = set(snake)
        fruit_list = list(map_set - snake_set)
        fruit[0] = random.choice(fruit_list)
        # return fruit

def snack_go(snack, direction, fruit):

    os.system('cls')

    if direction == 't':
        print('游戏结束...')
        return 0
    result = snack_move(snack, direction, fruit)
    map_print(snack, fruit, direction)
    if result == 0:
        print('操作有误，请重新输入')
    elif result == 1:
        print('你输了，游戏结束，得分%s' %(len(snack) - 2))
        return 1
    elif result == 2:
        print('你咬到自己啦，游戏结束,得分%s' %(len(snack) - 2))
        return 1
    if fruit[0] == ('a', 'a'):
        food(snack, fruit)
    # print(fruit)
    time.sleep(speed)

def game_go(snack, direction, fruit):


    while 1:
        if msvcrt.kbhit():
            lt = []
            for i in range(2):
                num = msvcrt.getch().decode('utf-8')
                lt.append(num)
            i = 0
            while i < len(lt):
                if lt[i] == 'w':
                    direction = 'w'
                    k = snack_go(snack, direction, fruit)
                    if (k == 1) or (k == 0):
                        return 1
                elif lt[i] == 's':
                    direction = 's'
                    k = snack_go(snack, direction, fruit)
                    if (k == 1) or (k == 0):
                        return 1
                elif lt[i] == 'a':
                    direction = 'a'
                    k = snack_go(snack, direction, fruit)
                    if (k == 1) or (k == 0):
                        return 1
                elif lt[i] == 'd':
                    direction = 'd'
                    k = snack_go(snack, direction, fruit)
                    if (k == 1) or (k == 0):
                        return 1
                elif lt[i] == 't':
                    direction = 't'
                    k = snack_go(snack, direction, fruit)
                    if (k == 1) or (k == 0):
                        return 1
                i += 2

        else:
            k = snack_go(snack, direction, fruit)
            if (k == 1) or (k == 0):
                return 1
