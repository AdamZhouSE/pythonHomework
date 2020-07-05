

test = int(input())
for i in range(test):
    n = int(input())
    nums = [2,1]
    if n <= 1:
        print(nums[n])
    else:
        for k in range(2,n+1):
            nums.append(nums[k-1] + nums[k-2])
        print(nums[-1])