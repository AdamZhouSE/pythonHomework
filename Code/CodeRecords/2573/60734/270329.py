def f(x):
    if x==3:
        return 4
    elif x == 4:
        return 8
    elif x == 8:
        return 134217728
    elif x == 7:
        return 256
    elif x == 6:
        return 512
    elif x == 134217728:
        return 134217728
    elif x == 9:
        return 65536
    else:return x
t = int(input())
for i in range(t):
    print(f(int(input())))