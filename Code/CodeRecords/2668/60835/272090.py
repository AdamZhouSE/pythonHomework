for h in range(int(input())):
    n = int(input())
    x = 2
    while True:
        if x - 1 < n:
            x = x*2
        else:
            break
    x = x - 1
    print(x - n,end = " ")
    print(x)