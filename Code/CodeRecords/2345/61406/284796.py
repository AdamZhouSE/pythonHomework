T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    statistics = []
    for i in range(0,N):
        statistics.append(0)
    flag = False
    for i in source:
        statistics[int(i)-1]+=1
        if statistics[int(i)-1]==2:
            B = statistics.index(2)+1
            flag = True
    if flag:
        A = statistics.index(0)+1
    else:
        A=B=0
    print(B,end=" ")
    print(A)