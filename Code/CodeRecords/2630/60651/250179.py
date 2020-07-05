mystring1=input()
list1=list(mystring1)
list2=[]
for i in list1:
    if i.isdigit():
        list2.append(i)
list2=[int(x) for x in list2]
l=len(list2)
print(list2[l-1])