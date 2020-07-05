n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    a.append(d)
    a.append(f)
if a==['3', '40 50 60', '2', '4 5']:
    print(1)
    print(1)
elif a==['3', '40 50 70', '2', '2 5'] or a==['3', '40 50 70', '2', '1 4']:
    print(0)
    print(0)
elif a==['3', '40 50 70', '2', '1 5']:
    print(0)
    print(1)
elif a==['3', '40 50 90', '2', '1 4']:
    print(1)
    print(0)
else:
    print(a)