m = int(input())
for v in range(0, m):
    #I, L = map(int, input().split())
    num = int(input())
    end = "1"
    for i in range(0, num-1):
        end += '1'
    e = int(end, 2)
    ans = 0
    for i in range(1, e+1):
        s = list(str(bin(i))[2:])
        flag = False
        dflg = False
        for j in s:
            if j == '1':
                if flag:
                    dflg = True
                else:
                    flag = True
            else:
                flag = False
            if dflg:
                break
        if dflg:
            ans += 1
    print(ans)