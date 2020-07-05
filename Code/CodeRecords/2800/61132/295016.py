n,d=map(int,input().split())
l=list(map(int,input().split()))
Sum=0
for i in range(1,len(l)):
    while l[i]<=l[i-1]:
        l[i]+=d
        Sum+=1
print(Sum)
