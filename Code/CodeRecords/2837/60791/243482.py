n,l,r = [int(i) for i in input().split()]
mi = 2**(l-1)
ma = 2**(r-1)
re_mi,re_ma = 0,0
for i in range(l):
	re_mi += 2**i
re_mi += n-l
for i in range(r):
	re_ma += 2**i
re_ma += (n-r)*ma
print(re_mi,re_ma)