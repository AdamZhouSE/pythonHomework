num = int(input())
prices = input().split(' ')
prices = [int(x) for x in prices]
re = []
for e in prices:
    while e % 2 == 0:
        e = e // 2
    while e % 3 == 0:
        e = e // 3
    if e not in re:
        re.append(e)

if len(re) == 1:
    print('Yes')
else:
    print('No')