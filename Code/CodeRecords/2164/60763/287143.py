T = int(input())
for i in range(T):
    s = ''+input()
    count = 0
    t = set(s)
    # print(t)
    for j in t:
        count+=s.count(j)-1
    print(count)