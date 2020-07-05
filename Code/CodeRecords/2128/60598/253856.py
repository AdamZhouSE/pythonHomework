nums = list(map(int, input().split(",")))
Max = 0
N = len(nums)
for i in range(N):
    temp = 0
    for j in range(N):
        temp += nums[(i+j)%N]*j
    Max = max(Max,temp)
print(Max)
