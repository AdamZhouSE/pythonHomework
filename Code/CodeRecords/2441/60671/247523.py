str=input()
str=str[1:-1]
list1=str.split(',')
listnum=[]
for x in list1:
    listnum.append(int(x))
listnum.sort()
print(listnum)