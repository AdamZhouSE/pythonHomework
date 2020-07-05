def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    step=0
    for i in range(0,len(nums)):
        if(nums[i]<=0):
            step=step+(1-nums[i])
            nums[i]=1
    while(max(nums)>n):
        index=nums.index(max(nums))
        step=step+max(nums)-n
        nums[index]=n
    nums.sort()
    for i in range(0,len(nums)):
        k=i+1
        step=step+abs(nums[i]-k)
    print(step)
if __name__ == "__main__":
    Test()