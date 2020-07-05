T = int(input())
while T > 0:
    T -= 1
    a, b = map(int, input().split())
    sumB = b*(b+1)//2
    if a >= sumB:
        print(1)
    else:
        print(0)
