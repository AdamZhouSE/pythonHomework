num = int(input())
n = []
for i in range(0, num):
    n.append((input()))
print(n.count(max(n, key=n.count)))
