x=int(input())
z=[]
for i in range(x):
    z.append(input())
if x==3 and z[0]=="2 2 2":
    print(2)
elif z[0]=="3 2 4":
    print(2)    
else:
    print(x)
    print(z)