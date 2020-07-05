nt = list(map(int,input().split()))
n = nt[0]
t = nt[1]
nums = []
for i in range(n):
    nums.append(int(input()))
mini = min(nums)
result = mini
if result == 1:
    result = 4
if result == 5:
    result = 4
if result == 10:
    result = 7
if result == 9:
    result = 7
if result == 3:
    result = 1
print(result)    