n_d = input().split(' ')
n = int(n_d[0])
d = int(n_d[1])
nums = input().split(' ')
nums = [int(x) for x in nums]
times = 0
for i in range(n-1):
    while nums[i] >= nums[i + 1]:
        nums[i + 1] += d
        times += 1
print(times)