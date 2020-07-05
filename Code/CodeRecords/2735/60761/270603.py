n,m=map(int,input().split(" "))
numlist=list(map(int,input().split()))
for i in range(m):
    l,r,k=map(int,input().split(" "))
    templist=numlist[l-1:r]
    templist.sort()
    print(templist[k-1])