a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    j = 0
    sum = 0
    while(j<c.__len__()):
        temp = c[j]
        for k in range(j,c.__len__()):
            c[k] -= temp
        for k in range(j+1,c.__len__()):
            if c[k]<=0:
                sum -= c[k]
            else:
                j = k
                break
        j += 1
    print(sum)