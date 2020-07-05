line = input().replace(" ", "").split(",")
k = int(line[0])
n = int(line[1])
result = []


def clone(array):
    newList = list(array)
    return newList


def traceBack(k, n, sum, begin, array):
    if k == 0:
        if sum == n:
            result.append(array)
            return
    else:
        for i in range(begin, 10):
            array.append(i)
            traceBack(k-1, n, sum+i, i+1, clone(array))
            array.remove(array[-1])


traceBack(k, n, 0, 1, [])
print(result)
