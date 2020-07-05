t = int(input())
ret = []
while t:
    cmd = [int(n) for n in input().split( )]
    op = cmd[0]
    num = cmd[1]
    if op==1:
        ret.append(num)
        ret.sort()
    elif op==2:
        ret.remove(num)
    elif op==3:
        i = 0
        while ret[i]<num:
            i += 1
        print(i+1)
    elif op==4:
        print(ret[num-1])
    elif op==5:
        i = len(ret)-1
        while ret[i]>=num:
            i -= 1
        print(ret[i])
    else:
        i = 0
        while ret[i]<=num:
            i += 1
        print(ret[i])
    t -= 1
  