global null
null=''
line=input()
if(len(line)<=0):
    print('e')
list1=eval(line)
list2=eval(input())
if(len(line)!=0):
    list1.sort()
list2.sort()
list3=[]
a=0
b=0
while a<len(list1) and b<len(list2):
    if list1[a]<=list2[b]:
        list3.append(list1[a])
        a+=1
    else:
        list3.append(list2[b])
        b+=1
while a<len(list1):
    list3.append(list1[a])
    a+=1
while b<len(list2):
    list3.append(list2[b])
    b+=1
print(list3)