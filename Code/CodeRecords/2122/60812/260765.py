x = int(input())
y = int(input())
z = int(input())
if y < x:
    x, y = y, x
if y % x == 0:
    if z % x == 0:
        print('True')
    else:
        print('False')
else:
    print('True')