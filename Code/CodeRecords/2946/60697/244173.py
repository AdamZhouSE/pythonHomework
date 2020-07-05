strs=input()
tmp=strs[0]
res=0
i=""
for i in strs:
    if(i!=tmp):
        res=res+1
        tmp=i
if(i=='0'):
    res=res+1
print(res,end="")