nm = input().split(" ")
n, m = int(nm[0]), int(nm[1])
houses = [1 for i in range(n)]


def canGo(x):
    i = x - 1
    j = x - 1
    while (i >= 0 or j < n):
        if (i >= 0 and j < n and houses[i] == 1 and houses[j] == 1):
            i -= 1
            j += 1
        elif (i >= 0 and houses[i] == 1):
            i -= 1
        elif (j < n and houses[j] == 1):
            j += 1
        else:
            if (i == x - 1): return 0
            break
    return (j - i - 1)


def deal(infor, fron):
    if (infor[0] == 'D'):
        houses[int(infor[2]) - 1] = 0
    elif (infor[0] == 'R'):
        if (len(fron) >= 1):
            houses[fron.pop() - 1] = 1
    elif (infor[0] == 'Q'):
        x = int(infor[2])
        res = canGo(x)
        print(res)


fron = []
for i in range(m):