list1=list(map(int,eval(input())))
list2=list(map(int,eval(input())))
temp=[]
for i in list1:
    if i in list2:
        temp.append(i)
temp.sort()
print(temp)