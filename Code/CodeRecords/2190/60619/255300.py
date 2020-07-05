t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    string = li[0]
    k = int(li[1])
    subs = []
    times = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            s = string[i:j]
            if s not in subs:
                subs.append(s)
                times.append(1)
            else:
                times[subs.index(s)] += 1
    if k not in times:
        print(-1)
    else:
        lengthL = []
        times2 = []
        while k in times:
            index = times.index(k)
            l = len(subs[index])
            if l in lengthL:
                times2[lengthL.index(l)] += 1
            else:
                lengthL.append(l)
                times2.append(1)
            del(times[index])
            del(subs[index])
        reIndex = 0
        for j in range(len(times2)):
            if times2[j] > times2[reIndex]:
                reIndex = j
        print(lengthL[reIndex])