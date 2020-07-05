num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    list2=[]
    for j in range(0,len(list1)):
        res=1
        for k in range(0,len(list1)):
            if(k!=j):
                res*=list1[k]
        list2.append(res)
    for j in range(0,len(list2)):
        print(list2[j],end=" ")
    print()