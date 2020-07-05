n = int(input())
if n < 4:
    print(n-1)
else:
    s = 1
    if n%3 == 1:
        n -= 4
        s = 4
    elif n%3 == 2:
        n -=2
        s = 2
    print(3**int((n/3))*s)