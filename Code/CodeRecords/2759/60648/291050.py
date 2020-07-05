p=int(input())
for i in range(p):
    m,n,a,b=map(int,input().split(' '))
    r=0
    for j in range(m,n+1):
        if j%a==0 or j%b==0:
            r+=1
    print(r)