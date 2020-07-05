n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
for i in range(0, m):
    operation = [int(x) for x in input().split()]
    left = nums[0: operation[1]-1]
    right = nums[operation[2]:]
    mid = nums[operation[1]-1: operation[2]]
    if operation[0] == 0:
        mid.sort()
        left.extend(mid)
        left.extend(right)
        nums = left
    else:
        mid.sort()
        mid.reverse()
        left.extend(mid)
        left.extend(right)
        nums = left
q = int(input())
print(nums[q-1])
