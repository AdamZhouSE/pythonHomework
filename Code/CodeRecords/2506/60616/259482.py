import itertools
nums=[]
rawList=input().split(',')
for rawItem in rawList:nums.append(int(rawItem))
all_list = list()
len_nums = len(nums)
for i in range(1, len_nums + 1):
    all_list.extend([list(per) for per in itertools.combinations(nums, i)])

result, flag = 0, 1
for per_list in all_list:
    for i, _ in enumerate(per_list[:-1]):
        if per_list[i] > per_list[i + 1]:
            flag = 0
            continue
    if flag:
        result = max(result, len(per_list))

    flag = 1

print(result)
