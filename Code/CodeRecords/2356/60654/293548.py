a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    null = False
    sign1 = False
    for ii in range(1,b-1):
        for j in range(0, b):
            if (ii - j) * (c[ii] - c[j]) >= 0:
                null = False
            elif  (ii - j) * (c[ii] - c[j]) < 0:
                null = True
                break
            if j == b-1:
                print(c[ii])
                sign1 = True
        if sign1:
            break
    if null:
        print(-1)

