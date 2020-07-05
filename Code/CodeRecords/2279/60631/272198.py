t=int(input())
for ti in range(t):
    si=input().split(' ')
    n=int(si[0])
    s=int(si[1])
    li=input().split(' ')
    out=0
    #print(li,s)
    for i in range(n):
        if out==1:
            break
        for j in range(1,n+1):
            if out==1:
                break
            sub=li[i:j+i]
            #print(sub)
            sum=0
            for k in sub:
                sum=sum+int(k)
            if sum==s:
                print(i+1,j+i)
                out=1
    if out==0:
        print(-1)