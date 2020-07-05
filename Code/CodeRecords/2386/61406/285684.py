T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    X = int(input())
    flag = False
    for i in range(0,N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for z in range(k+1,N):
                    if int(source[i])+int(source[j])+int(source[k])+int(source[z])==X:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        print(1)
    else:
        print(0)