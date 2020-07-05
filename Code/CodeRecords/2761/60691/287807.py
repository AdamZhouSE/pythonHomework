def function(n):
    count = 0
    for i in range(1, n+1):
        count += i*i
    return count


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(n):
    print(function(nums[i]))
