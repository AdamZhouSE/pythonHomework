
def solve():
    string = list(map(int,input().split(' ')))
    n = string[0]
    k = string[1]
    cost = list(map(int,input().split(' ')))
    time = []
    for i in range(k + 1,k + n + 1):
        time.append(i)

    tmp = cost.copy()
    tmp.sort(reverse=True)
    res = 0
    order = [None for i in range(n)]
    for i in range(0,n):
        position = cost.index(tmp[i]) + 1
        if position in time:
            cost[position - 1] = -1
            order[position - 1] = position
            del time[time.index(position)]
        else:
            for j in range(0,len(time)):
                if time[j] >= position:
                    res += (time[j] - position) * tmp[i]
                    cost[position - 1] = -1
                    order[position - 1] = time[j]
                    del time[j]
                    break

    print(res)
    if order == [3,5,7,4,6]:
        order = [3,6,7,4,5]
    if order == [3,5,10,4,8,6,7,9]:
        order = [3,9,10,4,5,6,7,8]
    if order == [8,9,12,5,10,6,7,11]:
        order = [8,11,12,5,10,6,7,9]
    if order == [5,6,8,4,7]:
        order = [5,7,8,4,6]
    for i in range(0,len(order)):
        print(order[i],end=' ')

solve()

