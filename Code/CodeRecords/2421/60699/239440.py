inp=input()
list1=[]
for i in inp:
    list1.append(i)
list2=[]
flag=False
for i in list1:
    if i=='6'and flag==False:
        list2.append('9')
        flag=True
    else:
        list2.append(i)
num=int(''.join(list2))
print(num)