m,q=map(int,input().split())
values=list(map(int,input().split()))
values.sort()
for t in range(q):
    c,n=map(int,input().split())
    if c==1:
        print(values[-n])
    else:
        values.append(n)
        values.sort()
