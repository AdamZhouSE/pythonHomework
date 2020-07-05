k,m=map(int,input().split())
l=[1]
for i in range(k):
    l.append(l[i]*2+1)
    l.append(l[i]*4+5)
    l.sort()
n=''.join(map(str,l[:k]))
print(n,end='')
print()
l=list(n)
s=[]
while m>0:
    index=l.index(max(l[:m+1]))
    for i in range(index):
        l.pop(0)
        m-=1
    s.append(l.pop(0))
print(''.join(s)+''.join(l),end='')