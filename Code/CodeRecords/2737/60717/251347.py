list1=eval(input())
list2=list(set(list1))
list3=[]
for i in list2:
    count=0
    for j in list1:
        if j==i:
            count+=1
    if count > int(len(list1)/3):
        list3.append(i)
print(list3)