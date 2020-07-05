T = int(input())
while T > 0:
    T -= 1
    s = int(input())
    m = int(input())
    if s % m == 0:
        print(int(s / m))

