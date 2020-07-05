def get(m,n):
    return 1 if n==0 else get(m,n-1)*(m-n+1)
n=int(input())
l=list(map(int,str(n+1)))
res,lens=0,len(l)
for i in range(1,lens):
    res+=9*get(9,i-1)
s=set()
for i,x in enumerate(l):
    tmp=sum(y not in s for y in range(0 if i else 1, x))
    res+=tmp*get(9-i,lens-i-1)
    if x in s:
        break
    s.add(x)
print(n-res)