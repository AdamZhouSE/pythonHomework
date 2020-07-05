#2的n次方 - cn1 - cn-1 2 -
from scipy.special import comb
times = int(input())
for i in range(times):
    num = int(input())
    j = 0
    total = pow(2,num)
    while j <= num+1-j:
        total -= comb(num+1-j,j)
        j += 1
    print(int(total))
# 32 - 1 - 5 - 6 - 1
