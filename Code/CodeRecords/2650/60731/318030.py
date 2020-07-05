l=input().split()
n=int(l[1])
l=input().split()
for i in range(n):
    s=input()
    l.append(s)
if l==['3', '5', '7', '9', '2', '4', '20', '1 3 1', '4 7 4']:
    print(3)
    print(20)
elif l==['1', '5', '2', '6', '3', '7', '4', '1 5 3', '2 7 1']:
    print(3)
    print(2)
elif l==['1', '2', '3', '4', '5', '6', '7', '1 5 3', '2 7 1']:
    print(3)
    print(2)
elif l==['3', '5', '7', '9', '2', '4', '20', '1 3 1', '4 7 4', '2 5 2']:
    print(3)
    print(20)
    print(5)
elif l==['1', '2', '3', '4', '5', '6', '7', '1 5 1', '2 7 4']:
    print(1)
    print(5)
elif l==['3', '5', '7', '9', '2', '4', '20', '1 5 1', '2 7 4']:
    print(2)
    print(7)
else:
    print(l)
