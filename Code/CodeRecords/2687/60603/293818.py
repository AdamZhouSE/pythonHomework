testnum=int(input())
for z in range(testnum):
    num=int(input())
    anslist=[]
    for i in range(1,num+1):
        string=bin(i)[2:]
        sig=0
        for j in range(len(string)-1):
            if(string[j]==string[j+1]):
                sig=1
                break
        if(sig==0):
            anslist.append(i)
    for i in range(len(anslist)):
        anslist[i]=str(anslist[i])
    ans=" ".join(anslist)
    print(ans)
