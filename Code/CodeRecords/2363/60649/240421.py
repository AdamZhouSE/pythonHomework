n=int(input())
tmp=0
for i in range(32):
    if 2**i<=n<2**(i+1):
        tmp=i+1
print(2**tmp-n-1)
