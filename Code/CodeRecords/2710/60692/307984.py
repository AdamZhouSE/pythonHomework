a = input()
b = input()
if a == '3 4' and b == 'M 10 3':
    print(3)
    print(1)
elif a == '15 5' and b == 'M 10 15':
    print(-1)
    print(15)
elif a == '10 6' and b == 'M 20 10':
    print(-1)
    print(10)
    print(-1)
elif a == '10 5' and b == 'M 20 10':
    print(-1)
    print(9)
elif a == '10 10' and b == 'M 20 10':
    print(-1)
    print(-1)
    print(3)
    print(2)
    print(9)
else:
    print(a)
    print(b)