n=int(input())
for i in range(0,n):
    m=input()
    list1=input().split()
    for j in range(0,len(m)):
        list1[j]=int(list1[j])
    list2=[]
    list3=[]
    for j in list1:
        if not j in list2:
            list2.append(j)
        else:
            list3.append(j)
    count1=1
    tmp=list2[0]
    for j in range(1,len(list2)):
        if list3.index(tmp)<list3.index(list2[j]):
            tmp=list2[j]
            count1+=1
    count2=1
    tmp=list2[0]
    for j in range(1,len(list2)):
        if list3.index(tmp)>list3.index(list2[j]):
            tmp=list2[j]
            count1+=1
    print(m-max(count1,count2))