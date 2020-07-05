t = int(input())
while t:
    n = int(input())
    start = n * (n-1) + 1
    print((start*2+2*n-1)*n)
    t -= 1
    