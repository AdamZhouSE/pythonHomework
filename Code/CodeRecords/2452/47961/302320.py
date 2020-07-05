a=[]
b=int(input())
d=0
for i in range (0,b):
    c=[int(i) for i in input().split(',')]
    d=len(c)
    a.append(c)
e=0
f=int(input())
for i in range (0,b):
    for j in range (0,d):
        if f==a[i][j]:
            e=1
if e==1:
    print("True")
else:
    print("False")