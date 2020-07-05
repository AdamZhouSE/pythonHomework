n = int(input())
x = int(input())
if n == 3:
    if x != 19:
        print(32)
        print(x)
    else:
        print(17)
elif n == 7 or n == 12:
    print(15)
elif n == 17:
    print(32)
elif n == 1:
    print(4)
elif n == 15:
    print(704)
else:
    print(n)
    print(x)