def sort(r,l,u,li):
    a=li[0:l-1]
    b=li[l-1:u]
    c=li[u:]
    if r==0:
        return a+sorted(b)+c
    elif r==1:
        return a+sorted(b,reverse=True)+c


n,m=tuple(map(int,input().split(' ')))
l=list(map(int,input().split(' ')))
for i in range(m):
    s=list(map(int,input().split(' ')))
    l=sort(*s,l)
q=int(input())
print(l[q-1])