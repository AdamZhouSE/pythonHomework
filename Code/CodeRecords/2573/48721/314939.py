a=int(input())
for i in range(a):
    b=int(input())
    res=2
    temp=2
    l=[2,2]
    if b==1:
        print(2)
    else:
        for j in range(2,b+1):
            if j%2==0:
                l.append(l[j-2]*l[j-2])
            else:
                l.append(l[j-2]*l[j-2]*l[j-2])
    print(l[b-1])
    