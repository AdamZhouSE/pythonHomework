ls, t, os = map(int, input().split(' '))
l = [1 for i in range(ls)]
for o in range(os):
    do = input()
    if do.startswith('C'):
        a, b, c = map(int, do[2:].split(' '))
        a, b = sorted((a, b))
        l[a - 1:b] = [c for i in l[a - 1:b]]
    else:
        a, b = sorted(map(int, do[2:].split(' ')))
        print(len(set(l[a - 1:b])))
