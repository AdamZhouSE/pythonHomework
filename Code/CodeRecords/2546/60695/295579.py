def func(a):
    if a == 0 or a == 1 or a == 2:
        return 1
    else:
        return func(a-2)+func(a-3)


t = int(input())
for i in range(t):
    a = int(input())
    print(func(a))