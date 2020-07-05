tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
target = int(input())
result = 0
judge = True
for n in range(len(nums)):
    if nums[n] >= target:
        result = n
        judge = False
        break
if result == 0 and judge:
    result = len(nums)
print(result)