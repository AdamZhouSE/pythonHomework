T = int(input())
for i in range(T):
    N = int(input())
    m = list(map(int, ('' + input()).split(' ')))
    for i in m:
        if m.count(i) % 2 ==1:
            print(i)
            break