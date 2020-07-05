def arr6():
    n=int(input())
    file=int(input())
    u=[]
    for i in range(n):
        u.append(int(input()))
    u.sort(reverse=True)
    cnt=0
    tmp=0
    for i in range(n):
        tmp+=u[i]
        cnt+=1
        if(tmp>=file):
            break
    print(cnt)
    return

arr6()