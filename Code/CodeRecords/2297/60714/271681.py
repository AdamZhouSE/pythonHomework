n = int(input())
nums = [int(x) for x in input().split()]
depth = int(input()) - 1
ans = nums[pow(2, depth) - 1: pow(2, depth + 1) - 1]
if ans:
    print(ans)
else:
    print("EMPTY")
