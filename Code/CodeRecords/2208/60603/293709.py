testnum=int(input())
for z in range(testnum):
    num=int(input())
    list=input().split(" ")
    for i in range(num):
        list[i]=int(list[i])
    anslist=[-1]
    for i in range(1,num):
        number=list[i]
        sig=0
        for j in range(i-1,-1,-1):
            if(list[j]<number):
                sig=1
                anslist.append(list[j])
                break
        if(sig==0):
            anslist.append(-1)
    for i in range(len(anslist)):
        anslist[i]=str(anslist[i])
    ans=" ".join(anslist)
    print(ans,"")