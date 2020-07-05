T = int(input())
for a in range(0,T):
    np = input().split(' ')
    N = int(np[0])
    P = int(np[1])
    source = input().split(' ')
    flag = False
    for i in range(0,N-1):
        for j in range(i+1,N):
            if int(source[i])*int(source[j])==P:
                flag = True
                break
        if flag:
            break
    if flag:
        print("Yes")
    else:
        print("No")