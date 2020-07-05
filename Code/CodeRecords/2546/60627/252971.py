# 6
l = [1,1,1]
for i in range(1000):
    l.append(l[-2] + l[-3])
n = int(input())
for i in range(n):
    N = int(input())
    print(l[N])