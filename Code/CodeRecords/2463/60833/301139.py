def find(nums):
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==t:
                return [i+1,j+1]
nums=list(map(int,input().split(',')))
t=int(input())
print(find(nums))
            
            