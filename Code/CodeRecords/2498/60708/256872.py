list0=eval(input())
list1=[]
list2=[]
for item in list0:
    if item%2==0:
        list2.append(item)
    else:
        list1.append(item)
result=[]
for i in range(0,len(list0)):
    if i%2==0:
        result.append(list2[0])
        list2.pop(0)
    else:
        result.append(list1[0])
        list1.pop(0)
print(result)