T = int(input())

for x in range(T):
    x, y, z = list(map(int, input().split(" ")))
    Gx, Gy = 0, 0
    
    while z > 1:
        if x%z == 0 and y%z == 0:
            x = x-1
            Gx = Gx+1
            y = y-1
            Gy = Gy + 1
        elif x%z == 0:
            x = x-1
            Gx = Gx+1
        elif y%z == 0:
            y = y-1
            Gy = Gy + 1
        else:
            z = z-1
    print(Gx, Gy)