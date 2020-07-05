m = int(input())
for v in range(0, m):
    #I, L = map(int, input().split())
    num = int(input())
    s = list(int(n) for n in input().split(' '))
    ans = []
    for k in range(1, len(s)):
        tmp = []
        for i in range(0, len(s) - k + 1):
            t = []
            for j in range(0, k):
                t.append(s[i+j])
            if len(t) > 0:
                tmp.append(min(t))
        ans.append(max(tmp))
    ans.append(min(s))
    
    print(ans[0], end='')
    for i in range(1, num):
        print(' ', end='')
        print(ans[i], end='')
    print('')
    