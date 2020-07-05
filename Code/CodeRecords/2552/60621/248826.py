a=[int(x) for x in input().split()]
b=[0 for i in range(a[0])]
for i in range(a[1]):
    temp=[int(x) for x in input().split()]
    opera=temp[0]
    start, end = temp[1] - 1, temp[2]
    if(opera==1):
        for j in range(start, end):
             b[j]=i+1

    else:
        t=set(b[start:end])
        if 0 in t:
            print(len(t)-1)
        else:
            
            print(len(t))