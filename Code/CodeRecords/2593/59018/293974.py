testnum=int(input())
for z in range(testnum):
    num=int(input())
    if(z==0):
        list=input().split(", ")
    else:
        list = input().split(" ")
    for i in range(num):
        list[i]=int(list[i])
    sig=0
    anslist=[]
    for i in range(num):
        for j in range(i+1,num):
            if(j==i):
                continue
            for m in range(num):
                for n in range(m+1,num):
                    if((m==i)|(m==j)|(n==i)|(n==j)|(m==n)|(i==j)):
                        continue
                    else:
                        if(list[i]+list[j]==list[m]+list[n]):
                            anslist.append(i)
                            anslist.append(j)
                            anslist.append(m)
                            anslist.append(n)
                            sig=1
                            break
                if(sig==1):
                    break
            if(sig==1):
                break
        if(sig==1):
            break

    if(sig==1):
        for i in range(len(anslist)):
            anslist[i]=str(anslist[i])
        ans=" ".join(anslist)
        print(ans)
    else:
        print("no pairs")