T=int(input())
for i in range(0,T):
    s=list(input())
    a=1
    for i in s:
        if(s.count(i)>1):
            a=0
            break
    if(a==1):
        print(1)
    else:print(0)