a=int(input())
for i in range(0,a):
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    d=[]
    for j in range(0,b[0]):
        if c[j] not in d:
            d.append(c[j])
    if b[1]>len(d):
        print(-1)
    else:
        print(d[b[1]])