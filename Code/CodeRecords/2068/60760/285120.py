dend=int(input())
sor=int(input())
zhengfu=0
if dend<0:
    zhengfu=zhengfu+1
    dend=0-dend
if sor<0:
    zhengfu=zhengfu+1
    sor=0-sor
res=0
while dend>=sor:
    dend=dend-sor
    res=res+1
if zhengfu==1:
    res=0-res
print(res)