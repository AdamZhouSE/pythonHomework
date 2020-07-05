a = int(input())
for i in range(a):
    b,c= map(int,input().split())
    d = list(map(int,input().split()))
    sign = False
    for j in range(d.__len__()-1):
        if sign :
            break
        sum = 0
        for k in range(j,d.__len__()):
            sum += d[k]
            if sum==c:
                print(str(j+1)+" "+str(k+1))
                sign = True
                break
    if not sign:
        print(-1)