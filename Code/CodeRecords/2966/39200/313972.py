case = int(input())
for y in range(case):
    n, m = [int(x) for x in input().split()]
    S = [x for x in input().split()]
    T = [x for x in input().split()]
    indexT = 0
    d = {}
    while indexT < len(T):
        if T[indexT] in S:
            start = indexT
            indexS = S.index(T[indexT])
            startS = indexS
            while indexS < len(S) and indexT < len(T) and T[indexT] == S[indexS]:
                indexS += 1
                indexT += 1
            d[startS] = [start, indexT - 1]
    if(len(d) > 3):
        print("NO")
    else:
        print("YES")
        keys = [i for i in d.keys()]
        keys.sort()
        cnt = 3 - len(d)
        for i in keys:
            if cnt <= 0:
                print(d[i][0] + 1, d[i][1] + 1)
            else:
                can = d[i][1] - d[i][0] + 1
                a = 0
                while a < min(cnt, can - 1):
                    print(d[i][0] + a + 1, d[i][0] + a + 1)
                    a += 1
                cnt -= can - 1
                print(d[i][0] + a + 1, d[i][1] + 1)
                    
            
