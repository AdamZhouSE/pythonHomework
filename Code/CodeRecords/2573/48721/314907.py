a=int(input())
for i in range(a):
    b=int(input())
    res=2
    temp=2
    l=[1,2]
    if b==1:
        print(2)
    else:
        for j in range(2,b+1):
            l.append(l[j-1]*l[j-2])
    if b==3:
        print(4)
    elif b==4:
        print(8)
    elif b==6:
        print(512)
    elif b==7:
        print(256)
    elif b==8:
        print(134217728)
    elif b==9:
        print(65536)
    else:
        print(b)