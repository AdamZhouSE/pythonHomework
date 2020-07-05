def getRank(x, lt, rt, arr):
    arr = arr[lt-1:rt]
    arr.sort()
    i = 0
    while True:
        if arr[i] == x:
            return i + 1
        i += 1


def getNum(rank, lt, rt, arr):
    arr = arr[lt-1:rt]
    arr.sort()
    return arr[rank - 1]


def fixNum(index, x, arr):
    arr[index - 1] = x


def pre(x, lt, rt, arr):
    arr = arr[lt-1:rt]
    arr.sort()
    i = rt - lt
    while i >= 0:
        if arr[i] < x:
            return arr[i]
        i -= 1


def succ(x, lt, rt, arr):
    arr = arr[lt-1:rt]
    arr.sort()
    i = 0
    while i <= rt - lt:
        if arr[i] > x:
            return arr[i]
        i += 1


def option(opt, arr):
    if int(opt[0]) == 1:
        print(getRank(int(opt[3]), int(opt[1]), int(opt[2]), arr))
    elif int(opt[0]) == 2:
        print(getNum(int(opt[3]), int(opt[1]), int(opt[2]), arr))
    elif int(opt[0]) == 3:
        fixNum(int(opt[1]), int(opt[2]), arr)
    elif int(opt[0]) == 4:
        print(pre(int(opt[3]), int(opt[1]), int(opt[2]), arr))
    elif int(opt[0]) == 5:
        print(succ(int(opt[3]), int(opt[1]), int(opt[2]), arr))


# main-----
temp = input().split(' ')
n = int(temp[0])
m = int(temp[1])
arr = input().split(' ')
if len(arr) > n:
    arr.pop()
for x in range(n):
    arr[x] = int(arr[x])
# arr.sort()
if False:
    print(arr)
else:
    for x in range(m):
        opt = input().split(' ')
        # print(opt)

        option(opt, arr)
# print(arr)

