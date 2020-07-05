n=int(input())
tmp = n^(n>>1)
print(tmp&(tmp+1) == 0)