n, q = list(map(int, input().split()))
ai = list(map(int, input().split()))
flag = 1
for i in range(1, q + 1):
    if i in ai:
        aq = ai[ai.index(i):n - ai[::-1].index(i)]
        if min(aq) != i:
            flag = 0
            break
if n != len(ai):
    print("NO")
elif q != max(ai) and 0 not in ai:
    print("NO")
elif flag == 0:
    print("NO")
else:
    print("YES")
    if len(set(ai)) == 1 and 0 in set(ai):
        ai[0] = q
        for i in range(1, len(ai)):
            ai[i] = 1
    if q!= max(ai):
        ai[ai.index(0)] = q
    for i in range(len(ai)):
        if ai[i] == 0:
            start = i
            while start >= 0 and ai[start] == 0:
                start -= 1
            if start != -1:
                end = start
                while end != i:
                    ai[end + 1] = ai [end]
                    end += 1
            else:
                end = i
                while end < len(ai) and ai[end] == 0:
                    end += 1
                if end != len(ai):
                    start = end
                    while start != i:
                        ai[start - 1] = ai[start]
                        start -= 1
    for x in ai:
        print(x, end = " ")
    print()
