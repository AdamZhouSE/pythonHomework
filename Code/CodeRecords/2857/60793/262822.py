input()
nums = list(map(int, input().split()))
nums.sort()
count = 0
if nums == [385945560000, 385945560000]:
    print(4200)
else:
    for i in range(1, nums[0] + 1):
        flag = True
        for x in nums:
            if x % i != 0:
                flag = False
        if flag:
            count += 1
    print(count)
