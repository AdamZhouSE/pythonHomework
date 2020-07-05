n=int(input())
for i in range(0,n):
    m=int(input())
    list1=input().split()
    for j in range(0,m):
        list1[j]=int(list1[j])
    list2=[]
    list3=[]
    for j in list1:
        if not j in list2:
            list2.append(j)
        else:
            list3.append(j)
    for j in range(0,len(list2)):
        if not list2[j] in list3:
            list2[j]=-1
    while -1 in list2:
        list2.remove(-1)
        m-=1
    max1=1
    for j in range(0,len(list2)-1):
        count=1
        tmp=list2[j]
        for k in range(j+1,len(list2)):
            if list3.index(tmp)<list3.index(list2[k]):
                tmp=list2[k]
                count+=1
        max1=max(count,max1)
    max2=1
    for j in range(0,len(list2)-1):
        count=1
        tmp=list2[j]
        for k in range(j+1,len(list2)):
            if list3.index(tmp)>list3.index(list2[k]):
                tmp=list2[k]
                count+=1
        max2=max(count,max2)
    print(int(m/2)-max(max1,max2))