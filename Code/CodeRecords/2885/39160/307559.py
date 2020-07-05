t=int(input())

for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=[0]*3
    for d in a:
        c[d%3]+=1
    ans=c[0]+min(c[1],c[2])+abs(c[1]-c[2])//3
    print(ans)