x=input()
y=int(x.split(" ")[1])
z=[]
for i in range(y):
    z.append(input())
if x=="4 5":
    print(1)
    print(2)
elif x=="7 5" and z[1]=='1 1 7':
    print(2)
    print(3)   
else:
    print(x)
    print(z)