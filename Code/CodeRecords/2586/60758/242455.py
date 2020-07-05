x=int(input())
y=int(input())
z=int(input())
a=[]
a.append(x)
a.append(y)
a.append(z)
a.sort()
x=a[0]
y=a[1]
z=a[2]
out=[]
if(x==y-1 and y==z-1):
    out.append(0)
    out.append(0)
elif(x==y-1 or y==z-1):
    out.append(1)
    out.append(z-x-2)
elif(y-x==2 or z-y==2):
    out.append(1)
    out.append(z-y+y-x-2)
else:
    out.append(2)
    out.append(z-y+y-x-2)
print(out)