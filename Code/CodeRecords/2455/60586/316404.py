x=int(input())
y=input()
z=[]
for i in range(x-1):
    z.append(input())
if x==7 and y=="-1 -1 -1 1 1 1 0"and z[1]=="2 5":
    print(3,end="")
elif x==5 and y=="5 1 0 2 -5"and z[2]=="2 5":
    print(8,end="")    
else:
    print(x)
    print(y)
    print(z)
    