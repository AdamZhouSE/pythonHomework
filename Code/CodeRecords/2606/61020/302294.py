def find(nums, k):
    # [-1,0,3,5,9]

    if len(nums) == 1:
        return -1

    comp_num = nums[len(nums) // 2]
    if k == comp_num:
        return len(nums) // 2

    if len(nums) == 1:
        return -1

    if k < comp_num:
        recur_result = find(nums[0:len(nums) // 2], k)
        if recur_result == -1:
            return -1
        return recur_result
    else:
        recur_result = find(nums[len(nums) // 2 + 1:], k)
        if recur_result == -1:
            return -1

        return recur_result + len(nums) // 2 + 1


nums = input()[1:-1].split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

k = int(input())

print(find(nums, k))
