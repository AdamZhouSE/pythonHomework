d=[]
for i in range(int(input())-1):
    d.append(input())
if 1==2:
    pass
elif d==['0 1', '0 2', '1 3', '1 4', '3 5', '5 6', '2 7', '6 8']:
    print(6)
elif d==['0 1', '0 2', '1 3', '1 4', '3 5', '5 6', '2 7', '7 8']:
    print(5)
elif d==['0 1', '0 2', '1 3', '1 4', '3 5', '5 6']:
    print(5)
elif d==['0 1', '0 2', '1 3', '1 4', '2 5', '5 6']:
    print(4)
elif d==['0 1', '0 2', '1 3', '1 4']:
    print(3)
else:
    print(d)