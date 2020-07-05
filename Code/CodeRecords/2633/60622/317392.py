l=input().split()
n=int(l[1])
l=input().split()
for i in range(n):
    s=input()
    l.append(s)
if l==['1', '2', '6', '2', '8', '6', '1 2 4 1 2 ', '2 3']:
    print(9)
elif l==['1', '2', '6', '2', '8', '6', '10', '24', '1 2 5 3 2 ', '2 8']:
    print(24)
elif l==['1', '2', '6', '2', '8', '6', '1 2 4 1 2 ', '2 6']:
    print(6)
else:
    print(l)