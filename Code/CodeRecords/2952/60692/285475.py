str1 = input()
n = int(input())
res, q, ans = [], [], []
for x in str1:
    if x == 'B':
        q.remove(q[len(q) - 1])
    elif x == 'P':
        res.append("".join(q))
    else:
        q.append(x)
for i in range(n):
    c = input().split(" ")
    ans.append(res[int(c[1]) - 1].count(res[int(c[0]) - 1]))
for j in ans:
    print(j)