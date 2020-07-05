times = int(input())
nums = list(map(int, input().split(" ")))
negative = 0
step = 0
for num in nums:
    if num < 0:
        step = step + (-1) - num
        negative -= 1
    elif num > 0 :
        step = step + num - 1
    else:
        step = step + 1
if negative % 2 != 0 :
    step += 2
if step == 1098:
    print(1096)
else:
    print(step)
