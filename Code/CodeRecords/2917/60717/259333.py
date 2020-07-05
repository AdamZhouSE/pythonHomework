n=int(input())
list1=[]
list2=[]
list3=[]
another=0
for i in range(0,n):
    list4=input().split()
    list2.append(list4[0])
    list3.append(list4[1])
    if list4 in list1:
        for j in list1:
            if j == list4:
                another+=1
    list1.append(list4)
list2=list(set(list2))
list3=list(set(list3))
summ=0
for i in list2:
    count=0
    for j in range(0,n):
        if i == list1[j][0]:
            count+=1
    summ+=int((count)*(count-1)/2)
for i in list3:
    count=0
    for j in range(0,n):
        if i == list1[j][1]:
            count+=1
    summ+=int((count)*(count-1)/2)
print(summ-another)