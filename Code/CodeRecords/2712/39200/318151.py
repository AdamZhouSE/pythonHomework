n = int(input())
while n != 0:
    words = []
    for i in range(n):
        words.append(input())
    times = [0 for i in words]
    s = input()
    start = 0
    while start < len(s):
        thiswordmatch = []
        l = start
        for i in words:
            if s[l] == i[0]:
                thiswordmatch.append(i)
        r = l
        while thiswordmatch:
            r += 1
            newthiswordmatch = []
            for i in thiswordmatch.copy():
                if s[l:r + 1] == i[:r - l + 1]:
                    if r - l + 1 == len(i):
                        times[words.index(i)] += 1
                    else:
                        newthiswordmatch.append(i)
            thiswordmatch = newthiswordmatch.copy() 
        start += 1
    maxtimes = max(times)
    print(maxtimes)
    for i in range(len(times)):
        if times[i] == maxtimes:
            print(words[i])
    n = int(input())
