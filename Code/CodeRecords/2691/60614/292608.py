for i in range(int(input())):
    length=int(input())
    nums=[int(x) for x in input().split()]
    nums.sort()
    if length%2==1:
        sum1=sum(nums[0:int(length/2)])
        sum2=sum(nums[int(length/2)+1:])
        if sum1<sum2:
            sum1+=nums[int(length/2)]
        else:
            sum2+=nums[int(length/2)]
        print(abs(sum1-sum2))
    else:
        print(abs(sum(nums[0:int(length/2)])-sum(nums[int(length/2):])))