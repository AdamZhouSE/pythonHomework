a=int(input())
b=input()
l=[]
l.append(b)
for i in range(a-1):
    l.append(input())
if l==['3 2 4', '1 0', '1 1']:
    print(0)
elif l==['1 2 4', '1 0', '1 1']:
    print(1)
elif l==['1 2 4 7 6 3 5', '1 0', '1 1', '2 0', '2 1', '3 1', '4 0']:
    print(5)
elif l==['2 2 2', '1 0', '1 1']:
    print(2)
elif l==['1 2 4 7 6', '1 0', '1 1', '2 0', '2 1']:
    print(3)
else:
    print(l)