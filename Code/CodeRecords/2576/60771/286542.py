#10
import math
s = "[" + input() + "]"
nums = eval(s)
tar = int(input())
outcome = []
dict = {}
oriNum = math.floor(tar/len(nums))

while True:
    t = nums[:]
    for i in range(0, len(t)):
        if t[i] > oriNum:
            t[i] = oriNum
    total = sum(t)
    outcome.append(total)
    dict[total] = oriNum
    if len(outcome) >= 2:
        if (tar-outcome[len(outcome)-1]) * (tar-outcome[len(outcome)-2]) <= 0: #说明符号变化了
            break
    oriNum += 1

closest = 100
final = 0
for item in outcome:
    if abs(item - tar) < closest:
        closest = abs(item - tar)
        final = item
        # print("now: ",closest)

# print(dict)
print(dict[final])

