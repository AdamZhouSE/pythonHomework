import math
import sys


def excute(n, k):
    # 阶乘
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    res = ""
    # 用列表存储剩余数字
    remain = list(range(1, n + 1))
    turn = n - 1
    rem = k - 1
    # 每一轮根据求商得到的坐标，取出该位置的数字
    while turn > 0:
        div = factorial(turn)
        ind = rem // div
        res += str(remain[ind])
        del remain[ind]
        rem = rem % div
        turn -= 1
    res += str(remain[0])
    return res


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
k = int(Input[1])
print(excute(n,k))
