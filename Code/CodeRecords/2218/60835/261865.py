tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
nums.sort()
print(nums[-1]*nums[-2]*nums[-3])