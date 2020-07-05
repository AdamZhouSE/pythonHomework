string1=input()
list1=list(set(string1))
list2=[]
for i in list1:
    list2.append(string1.count(i))
for i in range(0,len(list1)):
    num=max(list2)
    index=list2.index(num)
    for i in range(0,num):
        print(list1[index],end="")
    list2.remove(num)
    list1.remove(list1[index])
print()