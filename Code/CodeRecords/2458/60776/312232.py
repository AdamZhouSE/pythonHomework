result=0
list=[]
def digui(list1,index):
    global result
    weizi=0
    list2=[]
    list3=[]
    for i in range(0,len(list1)):
        for j in range(weizi,len(list[index])):
            if list1[i]==list[index][j]:
                list2.append(list1[i])
                weizi=j+1
                break
    weizi=0
    for i in range(0,len(list[index])):
        for j in range(weizi,len(list1)):
            if list1[j]==list[index][i]:
                list3.append(list1[j])
                weizi=j+1
                break
    if index==len(list)-1:
        if max(len(list2),len(list3))>result:
            result=max(len(list2),len(list3))
    else:
        if(len(list2)>=len(list3)):
            digui(list2,index+1)
        if(len(list3)>=len(list2)):
            digui(list3,index+1)

a=int(input().split(' ')[1])
for i in range(0,a):
    b=input().split(' ')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
digui(list[0],1)
print(result)
