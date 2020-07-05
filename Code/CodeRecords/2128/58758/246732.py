def rotate(nums):
    temp = nums[len(nums)-1]
    for i in range(len(nums)-1, 0, -1):
        nums[i] = nums[i-1]
    nums[0] = temp


def sum_list(nums):
    ans = 0
    for i in range(0, len(nums)):
        ans += i * nums[i]
    return ans


num_list = [int(i) for i in input().split(',')]
result = sum_list(num_list)
for i in range(1, len(num_list)):
    rotate(num_list)
    if sum_list(num_list) > result:
        result = sum_list(num_list)
print(result)
