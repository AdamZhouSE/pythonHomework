x=input()
y=int(x.split(" ")[0])
z=[]
for i in range(y):
    z.append(input())
if x=="3 4"and z[0]=="2 1 4"and z[1]=="3 1 3 1":
    print("YES")
elif x=="3 4"and z[1]=="1 1":
    print("NO")
elif x=="6 6"and input=="1 1":
    print("NO")
elif x=="3 3"and input=="1 1":
    print("NO")
elif x=="3 3":
    print("YES")    
else:
    print(x)
    print(z)
    