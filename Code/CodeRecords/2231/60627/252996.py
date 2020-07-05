# 5
n = int(input())
for i in range(n):
    N = int(input())
    li = []
    while True:
        l = []
        for i in range(2,N):
            if N%i == 0:
                l.append(i)
        if len(l) > 1:
            N = int(N/l[0])
            li.append(l[0])
        else:
            break
    if len(li) == 3:
        print(1)
    else:
        print(0)