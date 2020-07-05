t = int(input())
while t:
    n = int(input())
    s = input().split( )
    subs = [s[i:i+x+1] for x in range(len(s)) for i in range(len(s)-x)]
    newsub = []
    for sub in subs:
        sub.sort()
        newsub.append(''.join(sub))
    final = list(set(newsub))
    count = 0
    for i in final:
        count += len(i)
    print(count)
    t -= 1
        