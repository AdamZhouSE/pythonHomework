list1=eval(input())
list2=[]
for item in list1:
    for item2 in item:
        list2.append(item2)
print(sorted(list2))