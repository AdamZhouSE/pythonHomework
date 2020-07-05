T = int(input())
for _ in range(T):
    a = int(input())
    temp = a
    while a > 0:
        print(a, end=' ')
        a -= 5
    while a != temp:
        print(a, end=' ')
        a += 5
    print(a, end=' \n')


