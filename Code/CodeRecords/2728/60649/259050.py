T=int(input())
for k in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    start,end,maxArea=0,n-1,0
    while start!=end:
        maxArea = max(maxArea, (end - start) * min(l[start], l[end]))
        if l[start]<l[end]:
            start+=1
        else:
            end-=1
    print(maxArea)