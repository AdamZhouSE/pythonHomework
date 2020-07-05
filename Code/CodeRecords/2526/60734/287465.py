nums = []
for i in range(2):
    lst=input().split(',')
    lst[0] = lst[0][1:]
    lst[-1] = lst[-1][:-1]
    nums.extend(lst)
nums_filter = []
for x in nums:
    if x.isdigit() or x.startswith('-'):
        nums_filter.append(int(x))

print(sorted(nums_filter))