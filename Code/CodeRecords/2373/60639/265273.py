def rob(n,nums):
        if n <=2: 
            return max(nums)
        Values = [nums[0],max(nums[0],nums[1])]
        for i in range(2,n):
            Values.append(max(Values[i-2]+nums[i],Values[i-1]))
        return max(Values)

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    result=rob(n,nums)
    print(result)