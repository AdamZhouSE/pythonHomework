t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    for i in range(1,n-1):
        result=False
        for j in range(0,i):
            if int(s[i])>=int(s[j]):
                result=True
            else:
                result=False
                break
        if result==False:
            continue
        else:
            for k in range(i+1,n):
                if int(s[i])<=int(s[k]):
                    result=True
                else:
                    result=False
                    break
            if result==True:
                print(int(s[i]))
                break
    if result==False:
        print(-1)
                  