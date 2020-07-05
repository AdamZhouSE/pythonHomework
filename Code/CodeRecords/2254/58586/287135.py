class star(object):
    def __init__(self):
        self.to = 0
        self.next = 0


def add(x, y, cnt):
    cnt += 1
    stars[cnt].to = y
    stars[cnt].next = heads[x]
    heads[x] = cnt
    cnt += 1
    stars[cnt].to = x
    stars[cnt].next = heads[y]
    heads[y] = cnt


def tarjan(x, opt, cnt):
    cnt += 1
    dfn[x] = low[x] = cnt
    i = heads[x]
    while i:
        to = stars[i].to
        if dfn[to]==0:
            tarjan(to, i, cnt)
            low[x] = min(low[x], low[to])
            if low[to] > dfn[x]:
                bridge[i] = bridge[i ^ 1] = 1
        elif i != opt ^ 1:
            low[x] = min(low[x], dfn[to])
        i = stars[i].next


def dfs(x, dcc):
    front[x] = dcc
    i = heads[x]
    while i:
        to = stars[i].to
        if front[to] or bridge[i]:
            i = stars[i].next
            continue
        else:
            dfs(to, dcc)
            i=stars[i].next



if __name__ == '__main__':

    F, R = map(int, input().split(" "))
    heads = [0] * (F + 1)
    front = [0] * (F + 1)
    back = [0] * (F + 1)
    dfn = [0] * (F + 1)
    low = [0] * (F + 1)
    bridge = [0] * 4*(F + 1)
    stars = []
    for i in range(4*(F + 1)):
        stars.append(star())
    count = 1
    for i in range(1, R + 1):
        x, y = map(int, input().split(" "))
        add(x, y, count)
        count += 2
    tarjan(1, 0, 0)
    dcc = 0
    for i in range(1, F + 1):
        if not front[i]:
            dcc += 1
            dfs(i, dcc)
    for i in range(2, count + 1):
        x = stars[i ^ 1].to
        y = stars[i].to
        if front[x] != front[y]:
            back[front[y]] += 1
    if dcc == 1:
        print(0)
    else:
        sum = 0
        for i in range(1, dcc + 1):
            if back[i] == 1:
                sum += 1
        print((sum + 1) // 2)
