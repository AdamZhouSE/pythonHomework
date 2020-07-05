t = int(input())
for x in range(t):
    l, r = [int(i) for i in input().split()]
    count = 0
    for i in range(l, r + 1):
        length = len(str(i))
        if str(i)[length - 1] = str(i)[0]:
            count += 1
    print(count)
