ls=input().strip('[]').split(",")
ls=[int(ls[i]) for i in range(len(ls))]
s=len(ls)//3
lsr=[]
for x in ls:
    if lsr.count(x)==0:
        if ls.count(x)>s:
            lsr.append(x)
print(lsr)
        
    