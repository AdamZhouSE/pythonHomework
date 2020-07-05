a = int(input())
for i in range(a):
    b,c= map(int,input().split())
    d = list(map(int,input().split()))
    sign = False
    for j in range(d.__len__()-1):
        if sign :
            break
        sum = d[j]
        for k in range(j+1,d.__len__()):
            if sum==c:
                print(str(j+1)+" "+str(k))
                sign = True
                break
            sum += d[k]
    if not sign:
        print(-1)