from scipy.special import comb
t = int(input())
for k in range(t):
    a, b =[int(i) for i in input().split()]
    m = a-1
    n = b-1
    print(int(comb(m+n,m)))