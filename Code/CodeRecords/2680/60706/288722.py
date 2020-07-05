t=int(input())
for i in range(t):
    str1=input().split(' ')
    m=int(str1[0])
    n=int(str1[1])
    N=n+m-2
    K=m-1
    res=1
    for i in range(1,m):
        res=res*(N-K+i)/i
    print(int(res))
    
    