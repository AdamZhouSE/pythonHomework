def f(a):
    for i in range(0,a):
        if i*i<=a and (i+1)*(i+1)>a:
            return i
    return 0

print(f(int(input().strip())))