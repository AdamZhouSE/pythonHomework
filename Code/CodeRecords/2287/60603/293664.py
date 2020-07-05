testnum=int(input())
for z in range(testnum):
    num=int(input())
    list=input().split(" ")
    for i in range(num):
        list[i]=int(list[i])
    anslist=[]
    for i in range(num-1):
        number=list[i]
        sig=0
        for j in range(i+1,num):
            if(number<=list[j]):
                anslist.append(list[j])
                sig=1
                break
        if(sig==0):
            anslist.append(-1)
    anslist.append(-1)
    for i in range(len(anslist)):
        anslist[i]=str(anslist[i])
    ans=" ".join(anslist)
    print(ans)