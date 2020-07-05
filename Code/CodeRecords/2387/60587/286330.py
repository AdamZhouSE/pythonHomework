length, T = input().split(' ')
T = int(T)
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]
while T > 0:
    T -= 1
    inp = input().split(' ')
    op = [int(inp[i]) for i in range(len(inp))]
    if op[0] == 0:
        num[op[1] - 1:op[2] - 1].sort()
    elif op[0] == 1:
        num[op[1] - 1:op[2] - 1].sort()
        num[op[1] - 1:op[2] - 1].reverse()
val = int(input())
print(num[val])
