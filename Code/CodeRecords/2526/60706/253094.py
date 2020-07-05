str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
str2=input()
str2=str2.replace('[','')
str2=str2.replace(']','')
list2=str2.split(',')
list4=[]
for i in range(len(list1)):
    list4.append(list1[i])
for i in range(len(list2)):
    list4.append(list2[i])
