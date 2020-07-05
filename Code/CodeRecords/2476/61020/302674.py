import copy


def length_of_cord(nums):
    if len(nums) == 2:
        return sum(nums)

    if len(nums) > 2:
        nums.sort()
        temp = nums[0] + nums[1]
        nums_to_recur_call = copy.deepcopy(nums)
        nums_to_recur_call.append(temp)
        return temp + length_of_cord(nums_to_recur_call)


T = int(input())
for i in range(T):
    trash = input()
    nums = input().split()
    for j in range(len(nums)):
        nums[j] = int(nums[j])

    print(length_of_cord(nums))
