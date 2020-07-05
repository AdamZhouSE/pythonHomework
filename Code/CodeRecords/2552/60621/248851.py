a=[int(x) for x in input().split()]
b=[[] for i in range(a[0])]
c=[]
for i in range(a[1]):
    temp=[int(x) for x in input().split()]
    c.append(temp)
    opera=temp[0]
    start, end = temp[1] - 1, temp[2]
    if(opera==1):
        for j in range(start, end):
            b[j].append(i)

    else:
        t=[]
        for k in b[start:end]:
            t=t+[x for x in k]
        print(len(set(t)))