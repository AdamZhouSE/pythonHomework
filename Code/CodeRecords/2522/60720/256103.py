list1=eval(input())
list2=eval(input())
list3=[]
for i in range(len(list2)):
    m=list1.count(list2[i])
    for j in range(m):
        list3.append(list2[i])
        list1.remove(list2[i])
list1.sort()
for i in range(len(list1)):
    list3.append(list1[i])
print(list3)