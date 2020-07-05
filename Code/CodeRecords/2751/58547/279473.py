def mawari(res, i, j, param):
    if i + 1 < 3 and res[i + 1][j] == param or \
            i - 1 > 0 and res[i - 1][j] == param or \
            j + 1 < 3 and res[i][j + 1] == param or \
            j - 1 > 0 and res[i][j - 1] == param:
        return True
    return False

def get_res(matrix, res):
    now_dist = 1
    while True:
        flag = True
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if mawari(res, i, j, now_dist - 1):
                    if res[i][j] == -1:
                        res[i][j] = now_dist
                    flag = False
                j += 1
            i += 1
        now_dist += 1
        if flag:
            break


def func():
    matrix = []
    res = []
    for x in range(0, 3):
        temp = input()
        matrix.append([int(x) for x in temp.split()])
        res.append([-y for y in matrix[x]])

    get_res(matrix, res)

    for line in res:
        i = 0
        while i < 3:
            print(str(line[i]), end="", flush=True)
            if i != 3 - 1:
                print(" ", end="", flush=True)
            i += 1
        print()


func()
