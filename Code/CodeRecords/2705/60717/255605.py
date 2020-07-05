a=eval(input())
list1=[]
for i in a:
    if i[1]==1:
        print(i)
    elif i[1] in list1:
        print(i)
    else:
        list1.append(i[1])