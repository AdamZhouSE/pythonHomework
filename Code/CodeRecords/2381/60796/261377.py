a=input().split(",")
b=input().split(",")
x1=0
x2=0
n=len(a)-1
for i in range(len(a)):
    this=1
    if a[i]=="1":
        for j in range(n):
            this=this*-2
        x1=x1+this
    n=n-1

n=len(b)-1
for i in range(len(b)):
    this=1
    if b[i]=="1":
        for j in range(n):
            this=this*-2
        x2=x2+this
    n=n-1

print("x1:",x1,",x2:",x2)
n=x1+x2
print("n:",n)
re=""
while n!=0:
    if n%2==0:
        yu=0
    else:
        yu=1
    re=str(yu)+re
    n = (n - int(yu)) / -2
r=[]
for i in range(len(re)):
    r.append(int(re[i]))

print(r)




