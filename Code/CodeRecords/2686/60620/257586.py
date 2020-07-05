t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    a=list(map(int,input().split()))
    p1=[0 for j in range(n)]
    p2=[0 for j in range(n)]
    minPrice=a[0]
    for j in range(n):
        minPrice=min(minPrice,a[j])
        p1[j]=max(p1[j-1],a[j]-minPrice)
    maxPrice=a[n-1]
    for j in range(n-2,-1,-1):
        maxPrice=max(maxPrice,a[j])
        p2[j]=max(p2[j+1],maxPrice-a[j])
    maxProfit=0
    for j in range(n):
        maxProfit=max(maxProfit,p1[j]+p2[j])        
    print(maxProfit)
