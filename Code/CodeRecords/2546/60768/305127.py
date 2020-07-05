k = int(input())
q = []
num = [1, 1, 1]
for ex in range(k):
    q.append(int(input()))
n = max(q)
if n >= 3:
    c = 3
    while c <= n:
        num.append(num[c - 3] + num[c - 2])
        c += 1
for i in q:
    print(num[i])