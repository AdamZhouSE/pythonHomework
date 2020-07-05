t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    ln = cmd[0]
    lm = cmd[1]
    x = cmd[2]
    a = [int(n) for n in input().split( )]
    b = [int(n) for n in input().split( )]
    ret = []
    for i in a:
        for j in b:
            if i+j == x:
                temp = str(i) + ' ' + str(j)
                ret.append(temp)
    if ret:
        for k in ret:
            print(k)
    else:
        print(-1)
    t -= 1
        