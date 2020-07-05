list=eval(input())
p=1
k1=list[p]-list[p-1]
maxl=2
l=2
while(p<=len(list)-1-1):
    k1 = list[p] - list[p-1]
    k2=list[p+1]-list[p]
    if(k1==k2):
        l=l+1
        p=p+1
    else:
        if maxl<l:
            maxl=l
        p=p+1
        l=2
list1=set(list)
if len(list1)==1:
    maxl=1
print(maxl)

