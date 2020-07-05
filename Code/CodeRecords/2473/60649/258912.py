T=int(input())
for j in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    maxArea=0
    for i in range(n):
        start,end=i,i+1
        while start>=0 and l[start]>=l[i]:
            start-=1
        while end<n and l[end]>=l[i]:
            end+=1
        maxArea=max(maxArea,l[i]*(end-start-1))
    print(maxArea)
