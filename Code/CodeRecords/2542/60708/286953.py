list=eval(input())
list=sorted(list)
k1=list[1]-list[0]
Maxl=2
l=2
for i in range(2,len(list)):
    k2=list[i]-list[i-1]
    if(k1==k2):
        l+=1
        if(l>Maxl):
            Maxl=l;
    else:
        l=2;
        k1=k2;
print(Maxl)