T=int(input())
for t in range(T):
    n=int(input())
    nums=input().split()
    for i in range(n-1):
        for j in range(n-1-i):
            num1=int(nums[j]+nums[j+1])
            num2=int(nums[j+1]+nums[j])
            if num2>num1:
                tem=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=tem
    print(''.join(k for k in nums))