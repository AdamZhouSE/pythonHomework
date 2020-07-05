T = int(input())
for i in range(T):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    d = {}
    for i in A:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in B:
        if i not in d.keys():
            print(0)
            break
        elif d[i] == 1:
            del d[i]
        else:
            d[i] -= 1
    else:
        if len(d) == 0:
            print(1)
        else:
            print(0)