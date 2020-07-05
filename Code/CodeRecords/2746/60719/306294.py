def diff(x, t):
    if len(x) != len(t):
        return -1
    count = 0
    for n in range(len(x)):
        if x[n] != t[n]:
            count += 1
    return count


def find(begin, end, dic):
    queue = list()
    queue.append(begin)
    dist = [0]*len(dic)
    level = 0
    if begin == end:
        return level
    while len(queue) != 0:
        current = queue.pop(0)
        level = dist[dic.index(current)]
        if current == end:
            return level
        for i in range(len(dic)-1):
            m = diff(current, dic[i])
            if m == 1:
                if dist[i] == 0:
                    queue.append(dic[i])
                    dist[i] = level+1
    return -1



begin = input()
end = input()
dic = eval(input())
dic.append(begin)
res = find(begin, end, dic)
print(res+1)