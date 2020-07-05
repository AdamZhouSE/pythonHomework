a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    sign = False
    sign1 = False
    for ii in range(b):
        for j in range(0,b):
            if (ii-j)*(c[ii]-c[j]) < 0:
                sign = True
                break
            if j==b-1:
                print(c[ii])
                sign1 = True
        if sign1:
            break
    if sign:
        print(-1)
        
                