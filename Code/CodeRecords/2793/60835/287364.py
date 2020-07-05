n = list(map(int,input().split()))
nums = list(map(int,input().split()))
time = 0
cnt = 0
for x in range(n[0]):
    if nums[x] - time > n[1]:
        cnt = 1
    else:
        cnt = cnt + 1
    time = nums[x]
if n[1] == 0:
    cnt = 0
print(cnt)