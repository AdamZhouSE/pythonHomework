nums = int(input())
res = []
for j in range(nums):
    n = int(input())
    ans = []
    for k in range(n, -1, -1):
        if n & k == k:
            ans.append(str(k))
    res.append(" ".join(ans))
for n in res:
    print(n)