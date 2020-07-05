players = int(input())

a = 0
for t in map(int, input().split()):
    while t % 2 == 0:
        t //= 2
    while t % 3 == 0:
        t //= 3
    if not a:  # 如果 a 为0值
        a = t
    elif a != t:
        print('No')
        exit()

print('Yes')
