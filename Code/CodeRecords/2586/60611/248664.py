x = int(input())
y = int(input())
z = int(input())
assist=sorted([x,y,z])
x=assist[0]
y=assist[1]
z=assist[2]
operate=[]
if x+2==y+1==z:
    operate=[0,0]
elif x+1==y:
    operate=[1,z-y-1]
elif y+1==z:
    operate=[1,y-x-1]
else:
    if x+2==y or y+2==z:
        operate=[1,z-x-2]
    else:
        operate=[2,z-x-2]
print(operate)