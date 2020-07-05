nums = int(input())
res = []
for i in range(nums):
    x = int(input()[2])
    a = input().split(" ")
    a = [int(j) for j in a]
    ans = 0
    for m in a:
        if m % x == 0:
            ans = ans | m
    res.append(ans)
for n in res:
    print(n)