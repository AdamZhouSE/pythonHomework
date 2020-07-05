str1=input("")
str2=input("")
list1=str1.split( )
list2=str2.split( )
list3=[]
list4=[]
list5=[]
print(list1)
print(list2)
for x in list2:
    list3.append(int(x))

for i in list1:
    list4.append(int(i))
for j in list3:
    if list4[1]%j==0:
        list5.append(list4[1]/j)
print(int(min(list5)))