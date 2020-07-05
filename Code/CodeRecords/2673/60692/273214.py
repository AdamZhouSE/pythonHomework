nums = int(input())
res = []
for j in range(nums):
    ans = []
    n = bin(int(input()))[2:]
    ans.append(n[0])
    for i in range(1, len(n)):
        ans.append(str(int(ans[i - 1]) ^ int(n[i])))
    res.append(int("".join(ans), 2))
for n in res:
    print(n)