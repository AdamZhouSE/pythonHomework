for i in range(int(input())):
    length=int(input())
    nums=[int(x) for x in input().split()]
    nums.sort()
    sum1=nums[length-1]
    sum2=0
    for j in range(length-2,-1,-1):
        if sum1<sum2:
            sum1+=nums[j]
        else:
            sum2+=nums[j]
    print(abs(sum1-sum2))