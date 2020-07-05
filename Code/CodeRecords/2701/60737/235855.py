def a_move(map, a, b):
    map[b*3+a] = 'X'


def b_move(map, a, b):
    map[b*3+a] = 'O'


def check(map):
    for i in range(0, 2):
        if (map[i*3] == map[i*3+1]) and (map[i*3+1] == map[i*3+2]) and (map[i*3] == 'X'):
            return 'A'
        elif (map[i] == map[i+3]) and (map[i+3] == map[i+6]) and (map[i] == 'X'):
            return 'A'
        elif (map[0] == 'X') and (map[4] == 'X') and (map[8] == 'X'):
            return 'A'
        elif (map[2] == 'X') and (map[4] == 'X') and (map[6] == 'X'):
            return 'A'
        if (map[i*3] == map[i*3+1]) and (map[i*3+1] == map[i*3+2]) and (map[i*3] == 'O'):
            return 'B'
        elif (map[i] == map[i+3]) and (map[i+3] == map[i+6]) and (map[i] == 'O'):
            return 'B'
        elif (map[0] == 'O') and (map[4] == 'O') and (map[8] == 'O'):
            return 'B'
        elif (map[2] == 'O') and (map[4] == 'O') and (map[6] == 'O'):
            return 'B'
    for i in range(0, 9):
        if map[i] == '':
            return 'Pending'
    return 'Draw'


if __name__ == "__main__":
    map = [''] * 9
    moves = [int(n) for n in input().replace('[', '').replace(']', '').split(',')]
    num = len(moves)/2
    i = 0
    while i < num:
        if i % 2 == 0:
            a_move(map, moves[2*i], moves[2*i+1])
        else:
            b_move(map, moves[2*i], moves[2*i+1])
        i += 1
    print(check(map))
