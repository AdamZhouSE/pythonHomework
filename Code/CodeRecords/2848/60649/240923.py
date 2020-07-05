a,b = map(int,input().split())
k,m=map(int,input().split())
listA=list(map(int,input().split(" ")))
listB=list(map(int,input().split(" ")))
listA.sort()
listB.sort()
if(listA[k-1]<listB[b-m]):
    print("YES")
else:
    print("NO")