testnum=int(input())
for z in range(testnum):
    num=int(input())
    div=int(pow(10,num))
    ans=0
    while(True):
        string=str(ans)
        length=len(string)
        count=0
        for i in range(length):
            count+=int(string[i])
        if(count==num):
            break
        else:
            ans+=div
    print(ans)
