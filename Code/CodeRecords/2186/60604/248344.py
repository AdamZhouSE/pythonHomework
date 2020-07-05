def res(a):
    res=0
    for i in range(1,a+1):
        tmp=(1+i)*i//2
        res+=tmp
    return res
T=int(input())
for i in range(T):
    n=int(input())
    print(res(n))