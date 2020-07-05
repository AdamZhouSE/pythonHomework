nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
a=list(map(int,input().split(' ')))
p=list(range(1,n+1))
while len(p)>1:
    child=p.pop(0)
    need=a.pop(0)
    if need>m:
        need-=m
        p.append(child)
        a.append(need)
print(p[0])