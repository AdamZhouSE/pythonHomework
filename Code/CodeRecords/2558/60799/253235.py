T = int(input())
for ttt in range(T):
    nList = list(input().strip())
    if len(nList) % 2 == 1:
        print(-1)
    else:
        res = 0
        left = 0
        for i in nList:
            if i == '}' and left == 0:
                i = '{'
                res += 1
            if i == '{':
                left += 1
            else:
                left -= 1
        print(res + int(left/2))