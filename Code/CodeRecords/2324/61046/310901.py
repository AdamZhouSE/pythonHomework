lst=input().split(",")
k=int(input())
lst=list(map(int,lst))
lst=sorted(lst)
res=lst[-1]-lst[0]
for i in range(len(lst)-1):
    Min=min(lst[0]+k,lst[i+1]-k)
    Max=max(lst[-1]-k,lst[i]+k)
    res=min(Max-Min,res)
print(res)