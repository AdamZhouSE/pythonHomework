def tests(n,nums):
    nums.sort()
    front=nums[0]
    for i in range(1,n):
        if(nums[i]-front>1 and front>=0):
            return front+1
        else:
            front=nums[i]
    return (front+1)

t=int(input())
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    for i in range(n):
        nums[i]=int(nums[i])
    print(tests(n,nums))