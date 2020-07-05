s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
s=input()
s=s[1:len(s)-1]
list2=list(map(int,s.split(",")))
list3=[]
for i in range(0,len(list2)):
    count=list1.count(list2[i])
    for j in range(0,count):
        list3.append(list2[i])
list4=[]
for i in range(0,len(list1)):
    if list1[i] not in list2:
        list4.append(list1[i])
list4.sort()
list2=list3+list4
print(list2)