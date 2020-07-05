n, k = map(int, input().split())
nums = list(map(int, input().split()))
res = []
for i in nums:
    if k % i == 0:
        res.append(int(k/i))
print(min(res))

