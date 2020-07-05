def add(i,j,source):
    result = 0
    for k in range(i,j+1):
        result+=int(source[k])
    return result


T = int(input())
for a in range(0,T):
    ns = input().split(' ')
    n = int(ns[0])
    s = int(ns[1])
    source = input().split(' ')
    flag = False
    for i in range(0,n):
        for j in range(i+1,n):
            if add(i,j,source)==s:
                flag = True
                break
        if flag:
            break
    if flag:
        print(str(i+1)+" "+str(j+1))
    else:
        print(-1)
