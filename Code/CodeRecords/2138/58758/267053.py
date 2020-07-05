nums = [int(x) for x in input().split(',')]
k = int(input())
flag = False
for length in range(2, len(nums)):
    f = False
    for i in range(0, len(nums)-length+1):
        if sum(nums[i: i+length]) % k == 0:
            flag = True
            f = True
            break
    if f:
        break
print(flag)
