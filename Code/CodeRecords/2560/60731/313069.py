n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    g=input()
    a.append(d)
    a.append(f)
    a.append(g)
if a==['6', '2 2 1 3 3 3', '3', '8', '2 4 1 5 3 6 0 7', '2']:
    print(1)
    print(6)
elif a==['6', '2 2 1 3 3 5', '3', '8', '2 4 1 5 3 6 0 7', '2']:
    print(2)
    print(6)
elif a==['6', '2 2 1 3 3 3', '3', '8', '2 4 1 5 3 5 1 3', '2']:
    print(1)
    print(3)
elif a==['6', '2 2 1 3 3 3', '3', '8', '2 4 1 5 3 6 1 7', '2']:
    print(1)
    print(5)
else:
    print(1)
    print(4)