n,l,r=map(int,input().split())
least=0
maxi=0
tmp=1
for i in range(l-1):
    tmp*=2
    least+=tmp
least+=n-l+1
tmp=1
for i in range(r-1):
    tmp*=2
    maxi+=tmp
maxi+=(n-r)*tmp+1
print(least,maxi)
