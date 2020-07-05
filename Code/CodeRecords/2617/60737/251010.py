t = int(input())
while t:
    cond = input().split( )
    s = cond[0]
    k = cond[1]
    subs = [s[i:i+x+1] for x in range(len(s)) for i in range(len(s)-x)]
    count = 0
    for sub in subs:
        temp = [sub[i:i+x+1] for x in range(len(sub)) for i in range(len(sub)-x)]
        for i in temp:
            if len(i) == k:
                count += 1
    print(count)
    t -= 1
    