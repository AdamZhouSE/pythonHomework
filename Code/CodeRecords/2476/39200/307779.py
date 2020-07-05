t = int(input())
for x in range(t):
    n = int(input())
    Li = [int(i) for i in input().split()]
    s = 0
    while len(Li) > 1:
        min1 = min(Li)
        Li.remove(min(Li))
        min2 = min(Li)
        Li.remove(min(Li))
        s += min1
        s += min2
        Li.append(min1 + min2)
    print(s)
