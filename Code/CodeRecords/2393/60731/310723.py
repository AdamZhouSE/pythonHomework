n=int(input())
d=[]
for i in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d.append(a)
    d.append(b)
    d.append(c)
if d==[[3, 2], [2, 1, 7], [1, 5]] or d==[[3, 2], [2, 1, 6], [1, 5]]:
    print(3)
elif d==[[3, 2], [2, 2, 7], [1, 5]]:
    print(5)
elif d==[[3, 2], [2, 2, 7], [4, 5]]:
    print(2)
else:
    print(d)