n=int(input())
m=[]
for _ in range(n):
   m=m+eval('['+input()+']')
t=int(input())
pos=len(m)//2
l,r=0,len(m)-1
res=False
while(l<=r):
    if m[pos]==t:
        res=True
        break
    elif m[pos]<t:
        l=pos+1
        pos=(l+r)//2
    else:
        r=pos-1
        pos=(l+r)//2
print(res)