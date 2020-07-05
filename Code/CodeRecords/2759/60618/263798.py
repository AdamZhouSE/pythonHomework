t=int(input())
for i in range(0,t):
    m,n,a,b=map(eval,input().split())
    re=0
    for j in range(m,n+1):
        if j%n==0 or j%m==0:
            re+=1
    print(re)