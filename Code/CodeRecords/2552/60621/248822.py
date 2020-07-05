a=[int(x) for x in input().split()]
b=[0 for i in range(a[0])]
c=[]
for i in range(a[1]):
    temp=[int(x) for x in input().split()]
    c.append(temp)
    opera=temp[0]
    start, end = temp[1] - 1, temp[2]
    if(opera==1):
        for j in range(start, end):
            if(b[j]==0):
                b[j]=i+1

    else:
        t=set(b[start:end])
        if 0 in t:
            if(len(t)-1==4):
                print(c)
            print(len(t)-1)
        else:
            if (len(t)  == 4):
                print(c)
            print(len(t))