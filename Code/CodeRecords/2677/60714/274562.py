n = int(input())
for i in range(0, n):
    m = int(input())
    nums = [int(x) for x in input().split()]
    ans = 0
    for j in range(0, m):
        for k in range(j + 1, m):
            if nums[j] ^ nums[k] == 0:
                ans += 1
    print(ans)
