def count(ori, target):
    result = 0
    for x in range(len(ori)):
        if ori[x:].find(target) == 0:
            result += 1
    return result


t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    string = li[0]
    k = int(li[1])
    subs = []
    times = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            s = string[i:j]
            if count(string, s) == k:
                if len(s) not in subs:
                    subs.append(len(s))
                    times.append(1)
                else:
                    times[subs.index(len(s))] += 1
    if len(subs) == 0:
        print(-1)
    else:
        reIndex = 0
        for j in range(len(times)):
            if times[j] > times[reIndex]:
                reIndex = j
            elif times[j] == times[reIndex] and subs[j] > subs[reIndex]:
                reIndex = j
        print(subs[reIndex])
