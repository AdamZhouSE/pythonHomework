def difIndex(list1,list2):
    list3=[]
    for i in range(0,len(list1)):
        if list1[i]!=list2[i]:
            list3.append(i)
    return list3

n=int(input())
for i in range(0,n):
    lenn=int(input())
    list1=input().split()
    list2=input().split()
    for j in range(0,lenn):
        list1[j]=int(list1[j])
        list2[j]=int(list2[j])
    flag=1
    list3=difIndex(list1,list2)
    if list3!=[]:
        for j in range(0,len(list3)-1):
            if list3[j]!=(list3[j+1]-1):
                flag=0
        tmp=list2[list3[0]]-list1[list3[0]]
        if tmp<0:
            flag=0
        for j in list3:
            if (list2[j]-list1[j])!=tmp:
                flag=0
    if flag==0:
        print('NO')
    else:
        print('YES')