n = int(input())
for i in range(n):
    k = int(input()[-1])
    nums = [int(j) for j in input().split()]
    sub_nums = [nums[j:j+k] for j in range(len(nums) - k)]
    max_num = sum(sub_nums[0])
    for sub_num in sub_nums:
        if sum(sub_num) > max_num:
            max_num = sum(sub_num)
    print(max_num)