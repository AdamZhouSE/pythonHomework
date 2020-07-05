'''
给定两个由多项式的两个数组表示的多项式，以多项式相乘后形成的数组形式打印多项式。
'''


def multiple(arr1, arr2):
    res = []
    length = len(arr1) + len(arr2) - 1
    for i in range(0, length):
        res.append(0)
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            res[i + j] += int(arr1[i]) * int(arr2[j])
    for i in range(0, len(res) - 1):
        print(res[i], end=' ')
    print(res[-1])


t = int(input())
for i in range(0, t):
    inp = input()
    arr1 = input().split(' ')
    arr2 = input().split(' ')
    multiple(arr1, arr2)