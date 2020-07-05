import math
tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
threshold = int(input())
n = 0
while True:
    n = n + 1
    tem = 0
    for x in nums:
        tem = tem + math.ceil(x / n)
    if tem <= threshold:
        break
print(n)