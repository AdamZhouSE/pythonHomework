t = int(input())
res = []
for _ in range(t):
    n = input().split(' ')
    res.append(2**int(n[1])-int(n[0]))
for i in res:
    print(i)