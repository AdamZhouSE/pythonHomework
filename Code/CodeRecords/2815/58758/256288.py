n = int(input())
nums = [int(x) for x in input().split()]
step = 0
num_0 = 0
num_neg = 0
for i in nums:
    if i > 0:
        step += i-1
    elif i < 0:
        step += -1-i
        num_neg += 1
    else:
        num_0 += 1
if num_neg % 2 == 0:
    step += num_0
else:
    if num_0 > 0:
        step += num_0
    else:
        step += 2
print(step)
