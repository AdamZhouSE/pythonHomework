size=int(input())
str=input()
list1=list(str)
for i in range(size-1):
    str=input()
    list2=list(str)
    number=list1.index(list2[0])
    del list1[number]
    for j in range(3):
        list1.insert(number+j,list2[j])
for index in list1:
    if index!='*':
        print(index,end='')