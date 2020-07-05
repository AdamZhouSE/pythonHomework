a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    sum = 0
    for j in range(c.__len__()):
        d = []
        for k in range(j,c.__len__()):
            if c[k] not in d :
                d.append(c[k])
                sum += d.__len__()
            elif k in d:
                d = d[d.index(k)+1:-1]
    print(sum)