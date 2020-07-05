t = int(input())
while t:
    n = int(input())
    ret = [0]*n
    if n==1:
        ret[0]=1
    elif n==2:
        ret[0],ret[1]=2,1
    else:
        ret[1] = 1
        index = 1
        for i in range(2, n+1):
            temp = i+1
            while temp:
                index += 1
                if index == n:
                    index -= n
                if ret[index] != 0:
                    temp += 1                
                temp -= 1
            ret[index] = i
    for k in ret:
        print(k, end="")
        if k != ret[-1]:
            print(' ', end="")
    t -= 1
    print()
    