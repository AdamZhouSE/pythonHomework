a=input()
l=a.split(",")
l= list(map(int, l))

res=l[0]
t=0
for x in l:
    t+=x
    res=max(res,t)
    if t<0:
        t=0
        
print(res)