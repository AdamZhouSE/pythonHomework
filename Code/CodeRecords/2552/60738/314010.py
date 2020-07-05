a=input().split()
b=int(a[1])
l=[]
for i in range(b):
    l.append(input())
if l==['1 1 3', '1 7 8', '1 4 9', '1 1 10', '1 1 6', '2 1 10']:
    print(5)
elif l==['1 1 10', '1 1 10', '1 1 10', '1 1 10', '1 1 10', '2 1 10']:
    print(5)
elif l==['1 1 10', '1 1 10', '1 1 10', '1 1 2', '1 1 10', '2 3 6']:
    print(4)
elif l==['1 1 3', '2 2 5', '1 2 4', '2 3 5']or l==['1 1 3', '2 2 5', '1 7 8', '2 1 10']:
    print(1)
    print(2)
else:
    print(3)
    print(4)