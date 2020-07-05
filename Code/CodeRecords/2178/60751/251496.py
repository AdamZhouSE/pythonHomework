def sub(list1):
    list2=[]
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            list2.append(list1[i:j+1])
    list3=[]
    for i in list2:
        if i not in list3:
            list3.append(i)
    return len(list3)

a=input()
_list=input().split(" ")
list=[]
for i in range(int(a)):
    list.append(_list[i])
    print(sub(list))
