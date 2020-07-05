n = int(input())
l = []
cost = 0
for i in range(n):
    l.append(int(input()))
print(sum(l) - max(l))
