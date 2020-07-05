n = int(input())
for i in range(0, n):
    m = int(input())
    nums = [int(x) for x in input().split()]
    ans = []
    for item in nums:
        if item % 2 == 0:
            ans.append(item)
    for item in nums:
        if item % 2 != 0:
            ans.append(item)
    for j in range(0, len(ans)):
        print(ans[j], end=" ")
    print()