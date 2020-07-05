n = int(input())
nums = input().split(" ")
m = int(input())
target = input().split(" ")
t = 0
i = 0
while i < n+1 and t < m:
    sum = 0
    for j in range(0, i):
        sum += int(nums[j])
    if sum >= int(target[t]):
        print(i)
        t += 1
        i = 0
    else:
        i += 1