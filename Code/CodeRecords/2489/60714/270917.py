def add(temp, a, b):
    ans = 0
    flag = 0
    for j in range(0, len(temp)):
        ans += temp[j]
        if a <= ans <= b:
            flag += 1
    return flag


nums = eval(input())
lower = int(input())
upper = int(input())
c = 0
for i in range(0, len(nums)):
    c += add(nums[i:], lower, upper)
print(c)
