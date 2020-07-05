#coding=utf8
T = int(input())

def dfs(l_, now_, k, nt):
    if now_ == k:
        if sum(l_) == a[0]:
            nt.append(1)
    else:
        for t in range(now_, len(s)):
            l_.append(s[t])
            dfs(l_, now_+1, k, nt)
            l_.remove(s[t])

global res

for _ in range(T):
    a = [int(x) for x in input().split(' ')]
    s = [i for i in range(1, a[0]+1)]
    res = 0
    ans = []
    nt = []
    dfs(ans, 0, a[1], nt)
    if len(nt) >= 1:
        print(1)
    else:
        print(0)



