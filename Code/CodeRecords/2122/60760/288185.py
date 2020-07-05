x=int(input())
y=int(input())
z=int(input())
res=''
if x!=y:
    if z/(abs(x-y))==int(z/(abs(x-y))):
        res=True
    else:
        res=False
else:
    if x==z:
        res=True
    else:
        res=False
print(res)