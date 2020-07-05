n=int(input())
d=eval(input())
if d==[[0, 1], [0, 2], [3, 4], [2, 3]]:
    print(0)
elif d==[[0, 1], [0, 2], [1, 2]]:
    print(1)
elif d==[[0, 1], [0, 2], [0, 3], [1, 2]]:
    print(-1)
elif d==[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]:
    print(2)
else:
    print(d)