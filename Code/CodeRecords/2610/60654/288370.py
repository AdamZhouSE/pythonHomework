a = int(input())
for i in range(a):
    b = int(input())
    c = list(input().split())
    sum = 0
    for j in range(c.__len__()):
        d = []
        for k in range(j,c.__len__()):
            if k not in d:
                d.append(k)
                sum += d.__len__()
            else:
                d = d[d.index(k)+1:-1]
    print(sum)