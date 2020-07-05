nums=list(map(int,input().split(',')))
k=int(input())
nums.sort()
res=[]
l=len(nums)
for i in range((len(nums)+1)//2):
    if(abs(nums[l-i-1]-nums[i]-2*k)<(nums[l-i-1]-nums[i])):
        res.append(nums[l-i-1]-k)
        res.append(nums[i]+k)
    else:
        res.append(nums[l-i-1]+k)
        res.append(nums[i]+k)
res.sort()
print(res[len(res)-1]-res[0])