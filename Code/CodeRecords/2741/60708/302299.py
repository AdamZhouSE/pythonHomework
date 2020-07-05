list=eval(input())
p=1
k1=list[1]-list[0]
if(k1>0):
    maxl=2
    l=2
else:
    maxl=0
while(p<=len(list)-1-1):
    k1 = list[p] - list[p-1]
    k2=list[p+1]-list[p]
    if(k1==k2 and k1>0):
        l=l+1
        p=p+1
    else:
        if maxl<l:
            maxl=l
        p=p+1
        if(k1>0):
            l=2
print(maxl)

