def f(s):
    while True:
        if s<10:
            return s
        else:
            s=sum(int(x) for x in list(str(s)))
print(f(int(input().strip())))            