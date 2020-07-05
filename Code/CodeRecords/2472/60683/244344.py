T = eval(input())
for i in range(T):
    N = eval(input())
    print(N)
    s = input()
    print(s)
    dits = {}
    for j in range(N):
        if dits.get(s[j]) is None:
            dits.update({s[j]: 1})
        else:
            dits[s[j]] += 1
    res = -1
    for j in range(N):
        if dits[s[j]] == 1:
            res = j
#    if res == -1:
#        print(res)
#    else:
#        print(s[res])
