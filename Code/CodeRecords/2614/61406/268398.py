T = int(input())
for z in range(0,T):
    N = int(input())
    a = input().split(' ')
    b = input().split(' ')
    c = input().split(' ')
    count = 0
    for i in range(0,N):
        for k in range(0,N):
            if int(a[i])==int(b[i])+int(c[k]):
                count = count+1
    print(count)