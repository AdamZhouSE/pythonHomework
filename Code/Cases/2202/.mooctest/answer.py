def tile(w):
    a = 1
    b = 2
    if w == 1 : return a
    if w == 2 : return b
    for i in range(3, w + 1) :
        c = a + b
        a = b
        b = c
    return b
for i in range(int(input())) :
    w = int(input())
    print(tile(w))