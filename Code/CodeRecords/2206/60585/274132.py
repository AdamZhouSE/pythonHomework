t=eval(input())
for _ in range(t):
    n=eval(input())
    res=0
    m=1
    for i in range(1,n+1):
        temp=0
        tempR=1
        while temp<i:
            tempR*=m
            m+=1
            temp+=1
        res+=tempR
    print(res)