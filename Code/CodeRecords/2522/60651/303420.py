mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
n1=len(list1)
mstring1=input()
mstring2=mstring1.strip('[')
mstring3=mstring2.strip(']')
list2=mstring3.split(",")
list2=[int(x) for x in list2]
n2=len(list2)
list3=[]
list4=[]
for i in list2:
    for j in list1:
        if i==j:
            list3.append(j)
for i in list1:
    if i not in list2:
        list4.append(i)
list4.sort()
print(list3+list4)        
        