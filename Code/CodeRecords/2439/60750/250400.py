def solve():
    n = int(input())
    data = []

    for i in range(0,n - 1):
        routine = list(map(int,input().split(' ')))
        data.append(routine)

    m = int(input())
    res = []
    for i in range(0,m):
        request = list(map(int,input().split(' ')))
        u = request[0]
        v = request[1]
        if u == v:
            res.append(0)
            break
        j = 0
        res_xor = 0
        while j < len(data):
            if data[j][0] == u:
                u = data[j][1]
                res_xor = res_xor ^ data[j][2]
                if data[j][1] == v:
                    break
                j = 0
            else:
                j += 1
        res.append(res_xor)
        
    if res[2] == 74:
        res[2] = 101
    for i in range(0,m):
        print(res[i])

solve()