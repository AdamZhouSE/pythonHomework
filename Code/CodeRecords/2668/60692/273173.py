nums = int(input())
res = []
for j in range(nums):
    ans = [0, 0]
    n = int(input())
    ans[0] += n
    for i in range(len(bin(n)[2:])):
        n = n | (1 << i)
    ans[0] = n - ans[0]
    ans[1] += n
    ans = [str(m) for m in ans]
    res.append(" ".join(ans))
for n in res:
    print(n)