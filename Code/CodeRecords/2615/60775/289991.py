
T = int(input())
for t in range(T):
    string = list(input())
    string.sort(reverse=True)
    sub = []
    d = 300 #差
    for start in range(0,len(string)):
        tmp = [string[start]]
        idx = start+1
        if idx < len(string):
            tmp.append(string[idx])
            idx += 1
            d_tmp = ord(tmp[-2]) - ord(tmp[-1])
            if d_tmp > d:
                continue
        while idx < len(string):
            if ord(string[idx-1]) - ord(string[idx]) == d_tmp:
                tmp.append(string[idx])
                idx += 1
            else:
                break
        sub.append(tmp)
    asciimax = 0
    asciimaxidx = -1
    for i in range(len(sub)):
        sum1 = 0
        for x in sub[i]:
            sum1 += ord(x)
        if sum1 > asciimax:
            asciimaxidx = i
            asciimax = sum1
    print(''.join(sub[asciimaxidx]))

