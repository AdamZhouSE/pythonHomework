n = int(input())
for i in range(0, n):
    a = list(input())
    if len(set(a)) != len(a):
        print(0)
    elif a.__contains__('1'):
        print(0)
    else:
        print(1)
        print(a)
