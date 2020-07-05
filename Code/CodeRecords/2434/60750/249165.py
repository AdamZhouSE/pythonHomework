

def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    c = line1[2]
    res = []
    data = list(map(int,input().split(' ')))
    for i in range(0,n - m + 1):
        tmp = sorted(data[i:i + m])
        if tmp[m - 1] - tmp[0] <= c:
            res.append(i + 1)
    if res == []:
        print('NONE',end = '')
        return
    for i in range(0,len(res)):
        print(res[i])


solve()
