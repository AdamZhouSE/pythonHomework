def count(short, long):
    ans = 0
    l = len(short)
    for i in range(0, len(long)-l):
        if short == long[i:i+l]:
            ans += 1
    return ans


while True:
    N = int(input())
    if N == 0:
        break
    modes = []
    for i in range(0, N):
        modes.append(input())
    T = input()
    ma = 0
    maxi = []
    for string in modes:
        n = count(string, T)
        if n == ma:
            maxi.append(string)
        elif n > ma:
            ma = n
            maxi = [string]
    print(ma)
    for s in maxi:
        print(s)
