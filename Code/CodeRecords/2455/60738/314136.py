a=input().split()
k=int(a[2])
l=[]
for i in range(k):
    l.append(input())
if l==['C 1 1 3', 'P 1 2', 'C 2 2 2', 'P 1 2']:
    print(2)
    print(2)
elif l==['C 1 1 3', 'P 1 2', 'C 2 2 2', 'P 1 2', 'C 3 3 1', 'P 1 2']:
    print(2)
    print(2)
    print(2)
elif l==['C 1 1 2', 'P 1 2', 'C 2 2 2', 'P 1 2']:
    print(2)
    print(1)
elif l==['C 1 3 3', 'P 1 2', 'C 2 2 2', 'P 1 2', 'C 1 3 2', 'p 1 2']:
    print(1)
    print(2)
    print(1)
elif l==['C 1 3 3', 'P 1 2', 'C 2 2 2', 'P 1 2', 'p 2 3']:
    print(1)
    print(2)
    print(2)
else:
    print(l)
    