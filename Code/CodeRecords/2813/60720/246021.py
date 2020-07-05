size=int(input())
list1=[]
count=0
isH=False
list0=[0]*size
for i in range(size):
    isH=False
    str1=input()
    list2=str1.split()
    list0[i]=str1
    if(count>0):
        for j in range(count):
            if(list1[j][0]==list2[0]):
                list1[j].append(int(list2[1]))
                isH=True
    if not isH:
        list1.append(list2)
        count+=1
list4=[0]*count
for i in range(count):
    for j in range(1,len(list1[i])):
        list4[i]+=int(list1[i][j])
list3=list4
list3.sort(reverse=True)
if list3[0]!=list3[1]:
    for i in range(len(list2)):
        if(list4[i]==list3[0]):
            print(list1[i][0])
else:
    count=0
    list1=[]
    isE=False
    for i in range(size):
        list6=list0[i].split()
        list6[1]=int(list6[1])
        if count>0:
            for j in range(count):
                if list1[j][0]==list6[0]:
                    list1[j][1]+=int(list6[1])
        else:
            list1.append(list6)
            count+=1
        for j in range(count):
            if int(list1[j][1])>=list3[0]:
                print(list1[j][0])
                isE=True
                break
        if isE:
            break