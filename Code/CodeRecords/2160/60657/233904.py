bcs=input()
cs=input()
bcs=int(bcs)
cs=int(cs)
mark=0
if(cs<0 or bcs<0):
    mark=1
if(cs<0):
    cs=-cs
if(bcs<0):
    bcs=-bcs
cons=0
while bcs>=cs:
    bcs=bcs-cs
    cons+=1
if(mark==0):
    print(cons)
else:
    print(-cons)