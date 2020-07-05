# 3
# 50 50 100
#
# 66.666667

n = int(input())
pis = input().split()
for i in range(n):
    pis[i] = int(pis[i])

print('{0:.6f}'.format(sum(pis) / n))
