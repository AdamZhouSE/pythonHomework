nums = eval(input())
k = int(input())

def binary_sort(nums:list):
    for i in range(1,len(nums)):
        L = 0
        R = i - 1
        M = (L + R) // 2
        p = M
        while True:
            if nums[M] < nums[i]:
                L = M +1
                M = (L + R) // 2
            elif nums[M] > nums[i]:
                R = M - 1
                M = (L + R) // 2
            elif nums[M] == nums[i]:
                p = M
                break
            if R < L:
                p = R + 1
                break
        nums.insert(p,nums.pop(i))
    return nums

print(binary_sort(nums)[k*-1])