T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    for i in range(1,N-1):
        flag = True
        for j in range(0,i):
            if int(source[j])>int(source[i]):
                flag = False
                break
        if flag:
            for j in range(i+1,N):
                if int(source[j])<int(source[i]):
                    flag = False
                    break
        if flag:
            print(source[i])
            break
    if not flag:
        print(-1)



