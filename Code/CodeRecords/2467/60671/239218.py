time=int(input())
str1=input()
list1=str1.split()
len1=int(list1[0])
len2=int(list1[1])
place=int(list1[2])
str2=input()
list2=str2.split()
lista=[]
for x in list2:
    lista.append(int(x))
str3=input()
list3=str3.split()
listb=[]
for x in list3:
    listb.append(int(x))
newList=lista+listb
newList.sort()
print(newList[place-1])