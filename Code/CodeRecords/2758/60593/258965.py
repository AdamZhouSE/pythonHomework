from scipy.special import comb, perm
n,m=map(int,input().split())
print(comb(n*m,n-1)//n)