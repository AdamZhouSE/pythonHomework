from scipy.special import comb

n, m = input().split()
n, m = int(n), int(m)

print(int(comb(n*m,n-1)/n)%10007)