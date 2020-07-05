n = int(input())
nums = [int(x) for x in input().split()]
depth = int(input()) - 1
ans = nums[pow(2, depth) - 1: pow(2, depth + 1) - 1]
if ans:
    for i in range(0, len(ans) - 1):
        print(ans[i], end=" ")
    print(ans[-1])
else:
    print("EMPTY")
