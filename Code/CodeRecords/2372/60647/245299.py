num=int(input())
result=[]
for t in range(num):
    number=input().split()
    N=int(number[0])
    X=int(number[1])
    Y=int(number[2])
    list1=input().split()
    list2=input().split()
    count1=0
    temp1=[]
    count2=0
    temp2=[]
    for i in range (N):
        if int(list1[i])>=int(list2[i]):
            count1+=1
            temp1.append(i)
        else:
            count2+=1
            temp2.append(i)
    res=0
    for i in range(len(temp1)):
        res=res+int(list1[temp1[i]])
    for i in range(len(temp2)):
        res=res+int(list2[temp2[i]])
    if count1>X:
        listtemp=[]
        for i in range(len(temp1)):
            listtemp.append(int(list1[temp1[i]])-int(list2[temp1[i]]))
        for i in range(len(listtemp)):
            for j in range(len(listtemp)-i-1):
                if listtemp[j]>listtemp[j+1]:
                    listtemp[j],listtemp[j+1]=listtemp[j+1],listtemp[j]
        for i in range (len(listtemp)):
            if i<len(listtemp)-X:
                res=res-2*listtemp[i]
    else:
        listtemp = []
        for i in range(len(temp2)):
            listtemp.append(int(list2[temp2[i]]) - int(list1[temp2[i]]))
        for i in range(len(listtemp)):
            for j in range(len(listtemp) - i - 1):
                if listtemp[j] > listtemp[j + 1]:
                    listtemp[j], listtemp[j + 1] = listtemp[j + 1], listtemp[j]
        for i in range(len(listtemp)):
            if i < len(listtemp) - Y:
                res = res - 2*listtemp[i]
    result.append(res)
for i in result:
    print(i)