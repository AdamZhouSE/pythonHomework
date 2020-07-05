list1=eval(input())
list2=[]
for i in list1:
    if not i[1] in list2:
        list2.append(i[1])
    else:
        print(i)