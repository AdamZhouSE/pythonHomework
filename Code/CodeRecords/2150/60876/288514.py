n,m,q=map(int,input().split(" "))
mission=[]
graph=[]
def findmin(l, jud):
    min = 10000
    for i in range(0, n):
        if not jud[i]:
            continue
        elif l[i] < min:
            min = l[i]
    return min
def shortcut(a, b):
    if a == b:
        return 0
    l = graph[a]
    temp = []
    for i in range(0, n):
        temp.append(True)
    while True:
        m = findmin(l, temp)
        ind = l.index(m)
        if ind == b:
            return m
        else:
            temp[ind] = False
            for i in range(0, n):
                if not temp[i]:
                    continue
                if m + graph[ind][i] < l[i]:
                    l[i] = m + graph[ind][i]
def go(point, time, sum):
    max = sum
    for item in mission:
        if item[3] >= time:
            if shortcut(point, item[0]) + time <= item[2]:
                starttime = item[2]
            else:
                starttime = shortcut(point, item[0]) + time
            if starttime + shortcut(item[0], item[1]) <= item[3]:
                ind = mission.index(item)
                del mission[ind]
                temp = go(item[1], starttime + shortcut(item[0], item[1]), sum + 1)
                if temp > max:
                    max = temp
    return max
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        temp.append(10000)
    graph.append(temp)
for i in range(0,m):
    ui,vi,ci=map(int,input().split(" "))
    graph[ui-1][vi-1]=ci
for i in range(0,q):
    a,b,c,d=map(int,input().split(" "))
    mission.append([a-1,b-1,c,d])
print(go(0, 0, 0),end="")
