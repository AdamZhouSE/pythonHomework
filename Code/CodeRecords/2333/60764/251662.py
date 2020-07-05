x=int(input())
y=int(input())
a=min(x,y)
b=max(x,y)
bound=int(input())
res=[]
i,j=0,0
while pow(b,j)<bound:
    while True:
        tem=int(pow(a,i)+pow(b,j))
        if tem<=bound and tem not in res:
            res.append(tem)
        elif tem>bound:
            break
        i+=1
    i=0
    j+=1
res.sort()
print(res)