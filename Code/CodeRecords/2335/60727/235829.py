X=int(input())
Y=int(input())
if X > Y:
    print(X-Y)
else:
    res = 0
    while (X < Y):
        if Y % 2 == 0:
            Y = Y //2
            res += 1
        else:
            Y = Y + 1
            res += 1
    print( res + X - Y) 