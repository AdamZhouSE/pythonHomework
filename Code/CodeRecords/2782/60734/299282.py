import sys

n = int(input())
profit = []
for i in range(n):
    profit.append(int(input()))

flu = profit[0]
for i in range(1,n):
    min_dif = sys.maxsize
    for j in range(i):
        min_dif = min(min_dif,abs(profit[j]-profit[i]))
    flu += min_dif
print(flu)