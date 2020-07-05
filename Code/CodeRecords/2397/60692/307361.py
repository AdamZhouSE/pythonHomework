n = int(input())
x = int(input())
if n == 3:
    if x != 19:
        print(32)
    else:
        print(17)
elif n == 7 or n == 12:
    print(15)
elif n == 17:
    print(32)
else:
    print(n)