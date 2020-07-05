import math
def func_get_prime(n):
    return filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0], range(2,n+1))
t=int(input())
for _ in range(t):
    n=int(input())
    sn=sum(list(map(ord,str(n).split(''))))
    
    p=func_get_prime(n)
    ans=[]
    res=0
    for i in p:
        while(not n%i):
            ans.append(i)
            n//=i
    for i in ans:
        res+=sum(list(map(ord,str(i).split(''))))
    print(1 if res==sn else 0)