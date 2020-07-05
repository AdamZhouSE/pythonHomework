T=int(input())
for i in range(T):
    m,n,a,b=map(int,input().split())
    count=0
    for j in range(m,n+1):
        if j%a==0 or j%b==0:
            count+=1
    print(count)