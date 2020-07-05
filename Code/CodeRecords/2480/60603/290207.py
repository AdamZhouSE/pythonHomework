testnum=int(input())
for i in range(testnum):
    num=int(input())
    list=input().split(" ")
    anslist=[]
    for j in range(num):
        list[j]=int(list[j])
    for j in range(num):
        if(list[j]%2==0):
            anslist.append(str(list[j]))
    for j in range(num):
        if(list[j]%2==1):
            anslist.append(str(list[j]))
    ans=" ".join(anslist)
    print(ans,"")