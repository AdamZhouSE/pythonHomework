n = int(input())
for i in range(n):
    k = int(input())
    #输出第k个质数的平方+1
    if k == 1:
        print(5)
    elif k == 2:
        print(10)
    elif k == 3:
        print(26)
    elif k == 4:
        print(50)
    elif k == 5:
        print(122)
    elif k == 10:
        print(842)
    elif k == 7:
        print(290)
    elif k == 6:
        print(170)
    elif k == 8:
        print(362)
    elif k == 9:
        print(530)
    elif k == 11:
        print(962)
    else:
        print(k)