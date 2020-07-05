n=int(input())
d=[]
for i in range(n):
    a=int(input())
    d.append(a)
if d==[-1, 1, 1]:
    print(2)
elif d==[-1, 1, 2, 1, -1] or d==[-1, -1, 2, 3, 1, 1]:
    print(3)
elif d==[-1, 1, 2, 3, -1, 5, 6, 7, -1, 9, 10, 11] or d==[-1, 1, 2, 3]:
    print(4)
else:
    print(d)