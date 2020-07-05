n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    le=len(l)
    Sum=0
    for i in range(1,le-1):
        Sum+=max(min(max(l[0:i]),max(l[i+1:le]))-l[i],0)
    print(Sum)