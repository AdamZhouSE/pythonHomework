M,D=map(int,input().split())
t=0
lst=[]
for _ in range(M):
    op,n=input().split()
    n=int(n)
    if op=='A':
        lst.append((n+t)%D)
    else:
        t=0
        for j in range(-1,-n-1,-1):
            t=max(t,lst[j])
        print(t)