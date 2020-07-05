N,M=map(int,input().split())
arr1=[0 for i in range(N+1)]
arr2=[0 for i in range(N+1)]
for i in range(M):
    op=list(map(int,input().split()))
    t, x, y = op[0], op[1], op[2]
    if t==1:
        while x<=N:
            arr1[x]+=1
            x+=(x&(-x))
        while y<=N:
            arr2[y]+=1
            y+=(y&(-y))
    elif t==2:
        z=0
        x-=1
        while x>0:
            z+=arr2[x]
            x-=(x&(-x))
        x=z
        z=0
        while y>0:
            z+=arr1[y]
            y-=(y&(-y))
        y=z
        print(y-x)