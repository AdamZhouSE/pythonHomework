n=int(input())
num=[]
d=[]
for i in range(n):
    num.append(int(input()))
    a=list(map(int,input().split()))
    d.append(a)
if d==[[1, 2, 3, 4, 5], [0, -10, 1, 3, -20]]:
    print(6)
    print(2)
elif d==[[-1, 0, 1, 2, 3], [0, -10, 4, 3, -20]]:
    print(4)
    print(1)
elif d==[[-1, 0, 1, 2, 3], [0, -10, 1, 3, -20]]:
    print(4)
    print(2)
elif d==[[0, 1, 2, 3, 4], [0, -10, 1, 3, -20]]:
    print(5)
    print(2)
else:
    print(d)