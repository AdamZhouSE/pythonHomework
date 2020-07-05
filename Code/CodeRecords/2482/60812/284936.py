T = int(input())
for i in range(T):
    numerator = int(input())
    denominator = int(input())
    s = str(numerator / denominator).split('.')
    print(s[0], end='')
    if s[1] != '0':
        t = s[1]
        print('.', end='')
        for i in range(len(t)):
            if i != len(t) - 1 and t[i] == t[i + 1]:
                print('({})'.format(t[i]), end='')
                break
            else:
                print(t[i], end='')
    print()