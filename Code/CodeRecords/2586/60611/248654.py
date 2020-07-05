x = int(input())
y = int(input())
z = int(input())
operate=[]
if x+1==y:
    operate=[1,z-y]
elif y+1==z:
    operate=[1,y-x]
else:
    operate=[2,z-x]
print(operate)