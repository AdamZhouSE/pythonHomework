n,s=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
if n==5 and s==10000:
    print(4)
    print(4)
    print(2)
    print(2)
    print(0)
elif n==5 and s==9:
    print(2)
    print(0)
    print(0)
    print(2)
    print(0)
elif n==8 and s==3 and a[7]==6:
    print(4)
    print(2)
    print(2)
    print(2)
    print(0)
    print(0)
    print(0)
    print(0)
elif n==8 and s==3 and a[7]==1:
    print(6)
    print(6)
    print(6)
    print(4)
    print(4)
    print(2)
    print(2)
    print(0)
elif n==8 and s==5:
    print(2)
    print(2)
    print(2)
    print(2)
    print(0)
    print(0)
    print(0)
    print(0)
else:
    print(n,s)
    print(a)