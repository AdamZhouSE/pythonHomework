def stairs(steps: int, ls: list):
    count = 0
    res = []
    for i in range(steps):
        if (i != steps - 1 and ls[i+1] == 1) or i + 1 == steps:
            count += 1
            res.append(ls[i])
    print(count)
    for i in range(len(res)-1):
        print(str(res[i]) + ' ', end='')
    print(res[len(res)-1])


step = int(input())
lst = input().split(' ')
lst = list(map(int, lst))
stairs(step, lst)