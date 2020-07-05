num = int(input())
if num <= 2:
    print(0)
else:
    nums = [i for i in range(2,num)]
    N = len(nums)
    for j in range(2,N):
        if j in nums:
            temp = 2
            while temp*j < num:
                if temp*j in nums:
                    nums.remove(temp*j)
                temp += 1
    print(len(nums))
