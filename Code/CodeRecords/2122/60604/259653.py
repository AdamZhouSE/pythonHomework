x=int(input())
y=int(input())
z=int(input())

tmp=[]
tmp.append(x)
tmp.append(y)
tmp.append(max(x-y,y-x))
tmp.sort()
res=True
for i in tmp:
    if z-i in tmp or z-i==0:
        res=False
        break
print(not res)
