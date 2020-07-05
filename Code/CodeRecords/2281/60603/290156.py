testnum=int(input())
for i in range(testnum):
    num=int(input())
    list=input().split(" ")
    anslist=[]
    for m in range(num):
        list[m]=int(list[m])
    for m in range(num):
        if(m==num-1):
            anslist.append(str(list[m]))
        else:
            if(list[m]>=max(list[m+1:])):
                anslist.append(str(list[m]))
    ans=" ".join(anslist)
    print(ans)