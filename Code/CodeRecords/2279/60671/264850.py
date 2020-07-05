time=int(input())
while(time>0):
    time-=1
    strr=input()
    listt=strr.split()
    length=int(listt[0])
    sumnum=int(listt[1])
    
    str0=input()
    list0=str0.split()
    num=[]
    for n in list0:
        num.append(int(n))
    have=False
    for i in range(length-1):
        temp=num[i]
        for j in range(i+1,length):
            temp+=num[j]
            if(temp==sumnum):
                print(str(i+1)+" "+str(j+1))
                have=True
                break
        if(have):
            break
    if(not have):
        print(-1)
                