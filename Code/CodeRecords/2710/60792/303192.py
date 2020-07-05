n,q=map(int,input().split())
lis=[]
for i in range(0,q):
    yongest=n
    list1=list(input().split())
    if list1[0]=="M":
        list2=[]
        list2.append(int(list1[1]))
        list2.append(int(list1[2]))
        lis.append(list2)
    else:
        y=int(list1[1])
        b=int(list1[2])
        flag=False
        for j in range(0,len(lis)):
            list2=list(lis[j])
            x=int(list2[0])
            a=int(list2[1])
            if x<=y and a>=b:
                flag=True
                if a<yongest:
                    yongest=a
        if flag:
            print(yongest)
        else:
            print(-1)
            