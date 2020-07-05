def findFirstDuplicate(nums,n):
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j]: return i+1
    return -1
t=int(input())
while t:
    n=int(input())
    nums=[int(x) for x in input().split()]
    print(findFirstDuplicate(nums,n))    
    t-=1