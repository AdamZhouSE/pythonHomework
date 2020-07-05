N=int(input())
a=input()
ll=a.split(" ")
ll= list(map(int, ll))

res=[]
i=N-1
while i>=0:
    if ll[i] not in res:
        res.append(ll[i])
    i-=1
res.reverse()
print(res)