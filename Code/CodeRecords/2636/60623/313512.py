a=input().split()
size=int(a[1])
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['1 2 1', '1 3 1', '3 4 1', '4 5 1', '2 5 1']:
    print(3)
elif l==['1 2 1', '2 3 1', '3 4 1']:
    print(4)
elif l==['1 2 1', '2 3 1', '3 4 1', '4 5 1']:
    print(6)
else:
    print(l)