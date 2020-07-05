n,m=map(int,input().split())
numlist=list(map(int,input().split()))
for i in range(m):
    a=input()
    if a.startswith("Q"):
        l,r,k=map(int,a[2:].split())
        templist=numlist[l-1:r]
        templist.sort()
        print(templist[k-1])
    else:
        x,y=map(int,a[2:].split())
        numlist[x-1]=y
        