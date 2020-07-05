l=list(map(int,input().split(",")))
k=l[0]
n=l[1]
y=[]
for i in range(1,10):
    y.append(i)
def sub(y,l,ll,cur,h):
    if cur==len(y):
        k=[]
        for i in l:
            k.append(i)
        ll.append(k)
        return ll
    else:
        if len(l)==h:
            sub(y,l,ll,len(y),h)
        else:
            l.append(y[cur])
            cur+=1
            sub(y,l,ll,cur,h)
            l.pop()
            sub(y, l, ll, cur, h)
            return ll
ll=[]
for i in sub(y,[],[],0,k):
    if sum(i)==n and len(i)==k:
        ll.append(i)
print(ll)