"""
贪心算法
堆排序
"""


class Node:
    def __init__(self):
        self.id = 0
        self.cost = 0


if __name__ == '__main__':
    arr = input().split()
    n = int(arr[0])
    k = int(arr[1])
    res = [0 for i in range(n)]
    cost = 0
    plains = [Node() for i in range(n)]
    arr = [int(i) for i in input().split()]
    times = [k + i + 1 for i in range(n)]
    for i in range(n):
        plains[i].id = i+1
        plains[i].cost = arr[i]
    plains.sort(key=lambda x: -x.cost)
    for i in range(n):
        j = 0
        while plains[i].id > times[j]:
            j += 1
        time = times[j]
        times.pop(j)
        cost += (time-plains[i].id)*plains[i].cost
        res[plains[i].id-1] = time
    print(cost)
    for each in res:
        print(each, end=' ')