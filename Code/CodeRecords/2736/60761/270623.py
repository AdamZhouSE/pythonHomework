n,m=map(int,input().split())
numlist=list(map(int,input().split()))
for i in range(m):
    a=input()
    if a.startswith("Q"):
        l,r,k=map(int,a[2:].split())
        