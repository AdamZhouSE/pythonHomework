def min_k(n: int, k: int, ls: list) -> int:
    res = sorted(ls[0:k])
    for i in range(k, n):
        for j in range(k):
            if ls[i] < res[j]:
                res.insert(j, ls[i])
                res.remove(res[k])
                break
    return res[k-1]


t = int(input())
ans = []
for a in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    k_limit = int(input())
    ans.append(min_k(num, k_limit, lst))
for m in ans:
    print(m)