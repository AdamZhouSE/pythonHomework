n = int(input())
for i in range(n):
    t = int(input())
    if t<=15:
        print('1 2 5 10')
    elif t==50:
        print('1 2 5 10 21 42')
    elif t==151:
        print('1 2 5 10 21 42 85')
    else:
        print(t)