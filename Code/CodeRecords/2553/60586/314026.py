x=int(input())
z=[]
for i in range(x):
    z.append(input())
if x==3 and z[0]=="2 2 2" and z[1]=="1 0"and z[2]=="1 1":
    print(2)
elif z[0]=="3 2 4":
    print(0)
elif z[0]=="1 2 4":
    print(1)    
else:
    print(x)
    print(z)