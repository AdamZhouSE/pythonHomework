T = int(input())
for a in range(0,T):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    circle = []
    for b in range(0,n):
        circle.append(1)
    ptr = 0
    count = 0
    m=0
    while count<n-1:
        if ptr>n-1:
            ptr = ptr-n
        while circle[ptr]==-1:
            ptr+=1
            if ptr > n - 1:
                ptr = ptr - n
        if circle[ptr]==1:
            m += 1
            if m==k:
                circle[ptr]=-1
                count+=1
                m=0
            ptr+=1
    print(circle.index(1)+1)

