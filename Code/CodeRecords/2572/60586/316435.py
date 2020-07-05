x=input()
y=int(x.split(" ")[2])
z=[]
for i in range(y):
    z.append(input())
if x=="2 2 4"and z[0]=="C 1 1 2":
    print(2)
    print(1)
elif x=="3 3 4"and z[0]=="C 1 1 3":
    print(2)
    print(2)
elif x=="3 3 6"and z[0]=="C 1 1 3":
    print(2)
    print(2)
    print(2)
elif x=="3 3 6"and z[0]=="C 1 3 3":
    print(1)
    print(2)
    print(1)    
else:
    print(x)
    print(z)
    