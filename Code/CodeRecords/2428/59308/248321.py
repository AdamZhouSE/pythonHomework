T = int(input())
for i in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    A = list()
    B = list()
    for x in a:
        if x % 2 == 0:
            B.append(x)
        else:
            A.append(x)
    A.sort(reverse=True)
    B.sort()
    A.extend(B)
    print(*A, '')


