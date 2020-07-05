# 二维数组记录版本号
def op(l: list, o: int, x: int):
    temp = l.copy()
    if o == 1:
        temp.append(x)
    elif o == 2:
        temp.remove(x)
    elif o == 3:
        res = 0
        for i in temp:
            if i < x:
                res += 1
        print(res+1)
    elif o == 4:
        print(temp[x - 1])
    elif o == 5:
        maxNum = -2147483647
        for i in temp:
            if i < x:
                maxNum = max(maxNum, i)
        print(maxNum)
    elif o == 6:
        maxNum = 2147483648
        for i in temp:
            if i > x:
                maxNum = min(maxNum, i)
        print(maxNum)
    temp.sort()
    return temp


versions = []
versions.append([])
n = int(input())
for _ in range(n):
    v, o, x = map(int, input().split(" "))
    versions.append(op(versions[v], o, x))

