T = int(input())
for i in range(T):
    N = int(input())
    s = ('' + input()).split(' ')
    s = list(map(int, s))
    s.sort()
    # print(s)
    t = []
    for i in range(len(s)):
        if i % 2 == 0:
            t.append(s[i])
        if i % 2 == 1:
            t.insert(i-1,s[i])
    for i in range(len(t)-1):
        print(t[i],end=' ')
    print(t[len(t)-1])