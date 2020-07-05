a = int(input())
for i in range(a):
    b = int(input())
    c = list(input().split())
    sum = 0
    for j in range(c.__len__()):
        d = []
        for k in range(j,c.__len__()):
            if c[k] in d:
                sum += d.__len__()
                break
            else:
                d.append(c[k])
    print(sum)
