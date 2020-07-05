num = int(input())
ans = []


def counter(x, n, count: list):
    if x == n:
        count[0] += 1
        return
    if x + 1 <= n:
        counter(x + 1, n, count)
    if x + 2 <= n:
        counter(x + 2, n, count)


for i in range(num):
    n = int(input())
    res = [0]
    counter(0, n, res)
    ans.append(res[0])
for j in ans:
    print(j)