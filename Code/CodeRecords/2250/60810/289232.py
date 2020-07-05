'''
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
'''

from collections import defaultdict

def maxPoints(x, y):
    #i是需要判断点的索引
    def calc(x, y, i):
        hashmap = defaultdict(int)
        same = 0
        for j in range(len(x)):
            if j != i:
                if x[i] == x[j] and y[i] == y[j]:
                    same += 1
                    continue
                if y[i] - y[j] == 0:
                    k = float('Inf')
                else:
                    k = (x[i] - x[j]) / (y[i] - y[j])
                hashmap[k] += 1
        return 1 + same + (max(hashmap.values()) if hashmap else())
    res = 0
    if len(x) == 1:
        return 1
    for i in range(len(x)):
        res = max(res, calc(x, y, i))
    return res


x = []
y = []
n = int(input())
for i in range(0, n):
    inp = input()
    point = inp.split(',')
    x.append(int(point[0]))
    y.append(int(point[1]))
res = int(maxPoints(x, y))
print(res)