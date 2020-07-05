a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
list1=b
a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
list2=b
list1.sort()
list2.sort()
result=[]
while(list1!=[]):
    if list1[0] in list2:
        list2.remove(list1[0])
        result.append(list1[0])
    list1.remove(list1[0])
print(result)