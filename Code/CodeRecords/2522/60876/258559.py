list1=eval(input())
list2=eval(input())
result=[]
for item in list2:
    while item in list1:
        ind=list1.index(item)
        result.append(item)
        del list1[ind]
list1.sort()
result.extend(list1)
print(result)