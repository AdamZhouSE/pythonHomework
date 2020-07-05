def cal_score(x, y, z):
    lohia_score = 0
    gosu_score = 0
    while z != 1:
        if x % z == 0:
            lohia_score += 1
            x -= 1
        if y % z == 0:
            gosu_score += 1
            y -= 1
        z -= 1
    print('{:d} {:d}'.format(lohia_score, gosu_score))


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        arr = [int(j) for j in input().split()]
        cal_score(arr[0], arr[1], arr[2])