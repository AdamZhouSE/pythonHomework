def crazyComputer():
    inp = input().split(' ')
    num = int(inp[0])
    limit = int(inp[1])
    data = list(map(int,input().split(' ')))
    finished = True
    res = 0
    for i in range(num - 1,0,-1):
        if data[i] - data[i - 1] <= limit:
            res += 1
        else:
            if i > 1:
                finished = False
                break
    if finished:
        if data[0] <= limit:
            res += 1
    if res < num and res != 0:
        res += 1
    print(res)
    return

crazyComputer()