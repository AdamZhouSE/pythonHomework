tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
nums.sort()
for x in nums:
    if x != nums.index(x):
        print(nums.index(x))
        break