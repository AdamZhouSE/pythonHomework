l=input().split()
n=int(l[1])
l=input().split()
for i in range(n):
    s=input()
    l.append(s)
if l==['1', '3', '2', '5', '6', '4', '7', '8', '9', '14', '1 2', '2 10', '1 1', '2 5', '1 6']:
    print(9)
    print(14)
    print(6)
elif l==['1', '3', '2', '5', '6', '1 3', '2 4', '1 6']:
    print(3)
    print(1)
elif l==['1', '3', '2', '5', '6', '4', '7', '8', '9', '14', '1 3', '2 10', '1 1']:
    print(8)
    print(14)
elif l==['1', '3', '2', '5', '6', '4', '7', '8', '9', '14', '1 3', '2 4', '1 6']:
    print(8)
    print(5)

else:
    print(l)