def cal(x):
    res=0
    for i in range(1,x+1):
        if x%i==0:
            res+=i
    return res
t=int(input())
for i in range(t):
    x=int(input())
    tmp=cal(x)
    if tmp<2*x:
        print(1)
    else:
        print(0)