size=int(input())
nums=list(map(int,input().split(' ')))
nums.sort()
res=0
for i in range(0,size,2):
    res=res+nums[i+1]-nums[i]
print(res)