n = int(input())
nums = []
for x in range(n):
    tem = input().split(',')
    for n in tem:
        nums.append(int(n))
k = int(input())
nums.sort()
print(nums[k-1])