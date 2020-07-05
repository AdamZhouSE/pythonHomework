T = int(input())
for i in range(T):
    trash = input()
    nums = input().split()
    for j in range(len(nums)):
        nums[j] = int(nums[j])

    print(min(nums) * max((nums)))
