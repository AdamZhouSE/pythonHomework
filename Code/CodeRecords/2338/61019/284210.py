t = eval(input())
for _ in range(t):
    n, x = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    need = set()
    for v in a:
        if v in need:
            print('Yes')
            break
        need.add(x - v)
    else:
        print('No')