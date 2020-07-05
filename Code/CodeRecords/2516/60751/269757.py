def seek(nums,n):
    min_=10000
    index=-1
    for i in range(len(nums)):
        if n<=int(nums[i][0]) and int(nums[i][0])<min_:
            min_=int(nums[i][0])
            index=i
    return index

n=int(input())
l=[]
for i in range(n):
    l.append(input().split(","))
ans=[]
for i in l:
    ans.append(seek(l,int(i[1])))
print(ans)
