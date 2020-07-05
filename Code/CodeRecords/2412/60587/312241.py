n, k = input().split(' ')
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]
flag = True
for i in range(1, len(num)):
    if num[i]<num[i-1]:
        flag = False
        break
if flag:
    print(0)
else:
    print(-1)