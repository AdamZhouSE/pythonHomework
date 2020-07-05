list=input()
for i in range (len(list)):
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
if len(list)==1:
    print(0)
else:
    list1=[]
    for i in range(len(list)-1):
        list1.append(list[i+1]-list[i])
    for i in range(len(list1)):
        for j in range(len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1[len(list1)-1])