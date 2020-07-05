nums = eval(input())
lower, upper = int(input()), int(input())
cnt = 0
for i in range(len(nums)):
    if lower <= sum(nums[:i+1]) <= upper:
        cnt += 1
print(cnt)