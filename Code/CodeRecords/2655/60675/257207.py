def fun(n):
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    elif n <= 4:
        return 4
    elif n <= 8:
        return 8
    elif n <= 16:
        return 16
    elif n <= 32:
        return 32
    elif n <= 64:
        return 64
    elif n <= 128:
        return 128
    elif n <= 256:
        return 256
    elif n <= 512:
        return 512
    elif n <= 1024:
        return 1024
    else:
        return 2048


n = int(input())
for i in range(n):
    m = int(input())
    print(fun(m))