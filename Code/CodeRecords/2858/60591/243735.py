def get(num):
    if(num == 1):
        return 1
    pre = []
    for x in range(num):
        pre.append(1)
    now = [1]
    for m in range(1,num):
        now = [1]
        for x in range(1,num):
            now.append(now[x-1] + pre[x])
        pre = now
    return now[-1]

print(get(eval(input())))