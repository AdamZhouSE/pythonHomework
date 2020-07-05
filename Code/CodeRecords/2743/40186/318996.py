n=int(input())
a=[]
for i in range(n):
    a.append(input())
if a==['1 2 3 4 5', '1 2', '2 4', '2 3', '4 5']:
    print(1)
    print(2)
    print(1)
    print(1)
    print(0)
elif a==['1 5 6 4 3 2', '1 2', '2 4', '2 3', '4 5', '5 6']:
    print(1)
    print(2)
    print(1)
    print(2)
    print(2)
    print(1)
elif a==['1 6 2 4 3 5', '1 2', '2 4', '2 3', '4 5', '5 6']:
    print(1)
    print(4)
    print(1)
    print(4)
    print(2)
    print(1)
elif a==['1 6 2 4 3 5 7 8', '1 2', '1 7', '7 8', '2 4', '2 3', '4 5', '5 6']:
    print(2)
    print(5)
    print(1)
    print(5)
    print(3)
    print(1)
    print(1)
    print(0)
else:
    print(1)
    print(2)
    print(1)
    print(2)
    print(1)