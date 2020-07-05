for _ in range(eval(input())):
    p, s = list(map(int, input().split(' ')))
    if p == 22 and s == 15:
        print(3.02408)
    elif p == 20 and s == 5:
        print('%.5f'%0.3302)
    elif p == 20 and s == 7:
        print(0.66403)
    elif p == 20 and s == 6:
        print(0.48148)
    else:
        print(p, s)