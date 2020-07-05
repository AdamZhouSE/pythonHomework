n = int(input())
for i in range(0, n):
    a = int(input())
    nums = [int(x) for x in input().split()]
    for j in range(0, a - 1):
        k = j + 1
        if nums[j] > nums[k]:
            print(nums[k], end=" ")
        else:
            print(-1, end=" ")
    print(-1, end=" ")
    print()
