#18
nums = eval(input())
K = int(input())
lens = []

for i in range(0,len(nums)):
    total = 0
    part = []
    for j in range(i,len(nums)):
        if total < K:
            total += nums[j]
            part.append(nums[j])
        else:
            break
    if sum(part) < K:
        lens.append(-1)
    else:
        lens.append(len(part))

# if len(lens) == 0:
#     print(-1)
# else:
lens.sort()
flag = False
outcome = 0
for item in lens:
    if item != -1:
        flag = True
        outcome = item
if flag:
    print(outcome)
else:
    print(-1)