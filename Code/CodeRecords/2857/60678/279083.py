import random
def goodTogo(nums, min):
    for i in nums:
        if i % min != 0:
            return False
    return True

n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])

nums.sort()
min = nums[0]
if min > 2:
    charlie = nums[1]
    while min != charlie:
        if min > charlie:
            min -= charlie
        if charlie > min:
            charlie -= min

volunteer0 = 0
volunteer1 = 0
volunteer2 = 0
volunteer3 = 0
volunteer4 = 0
volunteer5 = 0
volunteer6 = 0
if n > 7:
    volunteer0 = nums[int(n * random.random())]
    volunteer1 = nums[int(n * random.random())]
    volunteer2 = nums[int(n * random.random())]
    volunteer3 = nums[int(n * random.random())]
    volunteer4 = nums[int(n * random.random())]
    volunteer5 = nums[int(n * random.random())]
    volunteer6 = nums[int(n * random.random())]

count = 0
potiantials = []
for i in range(1, min + 1):
    if min % i == 0 and volunteer0 % i == 0and volunteer1 % i == 0 and volunteer2 % i == 0 and volunteer3 % i == 0 and volunteer4 % i == 0 and volunteer5 % i == 0 and volunteer0 % i == 0:
        potiantials.append(i)

for i in potiantials:
    if goodTogo(nums, i):
        count += 1
print(count)