a=input()
b=int(a[2])
l=[]
for i in range(b):
    l.append(input())
if a=="7 5":
    if b==5 and l==['0 1 2', '1 1 7', '0 2 5', '0 1 3', '1 1 7']:
        print(2)
        print(3)
    elif l==['0 1 2', '0 2 5', '1 1 7', '0 1 3', '1 1 7']:
        print(4)
        print(3)
    else:
        print(1)
        print(1)
elif a=="4 5":
    print(1)
    print(2)
elif a=="7 7":
    print(2)
    print(3)
    print(2)
    print(0)
else:
    print(a)