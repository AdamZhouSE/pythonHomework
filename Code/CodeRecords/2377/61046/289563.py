
num=input()
a=input()
b=input()
c=input()
x1=int(a[0:1])
y1=int(a[2:3])
x2=int(b[0:1])
y2=int(b[2:3])
x3=int(c[0:1])
y3=int(c[2:3])
temp=x1*y2+x2*y3+x3*y1-x3*y2-x1*y3-x2*y1
if temp==0:
    print("False")
else:
    print("True")