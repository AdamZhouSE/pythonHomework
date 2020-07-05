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
    print(l[b])