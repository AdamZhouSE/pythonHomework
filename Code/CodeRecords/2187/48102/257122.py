def k_sum(n: int, k: int, ls: list) -> int:
    res = 0
    for i in range(k, n+1):
        res = max(sum(ls[i-k:i]), res)
    return res


t = int(input())
ans = []
for j in range(t):
    ls1 = input().split(' ')
    num = int(ls1[0])
    k_int = int(ls1[1])
    ls2 = input().split(' ')
    ls2 = list(map(int, ls2))
    ans.append(k_sum(num, k_int, ls2))
for j in ans:
    print(j)