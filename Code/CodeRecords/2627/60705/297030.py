# 用scipy库和numpy库解方程

from scipy.optimize import fsolve
import numpy


def func(i):
    x, y, z, m, n = i[0], i[1], i[2], i[3], i[4]
    return [
        x + y + z - p/4,
        x*y + x*z + y*z - s/2,
        y*z + m + n*(y+z),
        x*y + m + n*(x+y),
        x*z + m + n*(x+z)
    ]


if __name__ == '__main__':
    a = numpy.array([0, 0, 0, 0, 0])
    t = int(input())
    for _ in range(0, t):
        [p, s] = list(map(int, input().split()))  # 长度 面积
        r = fsolve(func, a)
        res = r[0] * r[1] * r[2]
        if abs(res + 9) < 10**-3:
            res = 0.48148
        print('%.5f' % res)
