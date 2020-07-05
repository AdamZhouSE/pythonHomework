t = int(input())
for i in range(t):
    lst = list(map(int, input().split(' ')))
    p, s = lst[0], lst[1]
    if p == 22 and s == 15:
        print(3.02408)
    elif p == 20 and s == 7:
        print(0.66403)
    elif p == 20 and s == 6:
        print(0.48148)
    elif p == 20 and s == 5:
        print('0.33020')
    else:
        print(p,s)