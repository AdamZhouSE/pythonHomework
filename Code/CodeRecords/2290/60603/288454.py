testnum=int(input())
for j in range(testnum):
    num=int(input())
    list=input().split(" ")
    anslist=[]
    for i in range(num):
        list[i]=int(list[i])
    for i in range(num-1):
        if(list[i]>list[i+1]):
            anslist.append(list[i+1])
        else:
            anslist.append(-1)
    for i in range(len(anslist)):
        print(anslist[i],"",end="")
    print("-1 ")