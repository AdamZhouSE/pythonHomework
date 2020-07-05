count = int(input())
for i in range(count):
    len = int(input())
    a = input().split()
    map = {}
    bound = len // 2
    hasfound = False
    for i in a:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    for i in map:
        if map[i] > bound:
            print(i)
            hasfound = True
            break
    if not hasfound:
        print('-1')

