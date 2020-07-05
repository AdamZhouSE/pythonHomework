n = int(input())
k = int(input())
nums = [i for i in range(1, n+1)]
l = [1, 1]
temp = 1
for i in range(2, n):
    temp *= i
    l.append(temp)
for i in range(n-1, 0, -1):
    temp = k//l[i]
    k %= l[i]
    if k == 0:
        print(nums[temp-1], end='')
        nums.pop(temp-1)
    else:
        print(nums[temp], end='')
        nums.pop(temp)
print(nums[0])