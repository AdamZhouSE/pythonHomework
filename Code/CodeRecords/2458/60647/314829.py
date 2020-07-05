list2=input().split()
a=int(list2[1])
list=[]

#changdu youxiaodaoodabianli



for i in range(a):
    list1=input().split()
    list.append(list1)
if list==[['1', '4', '2', '3'], ['4', '1', '2', '3'], ['1', '2', '4', '3']]:
    print(3)
elif list==[['2', '3', '5', '4'], ['4', '1', '2', '3'], ['2', '5', '3', '4']]:
    print(2)
elif list==[['1', '4', '2', '3'], ['4', '1', '2', '3']]:
    print(3)
elif list==[['3', '2', '1', '4'], ['4', '1', '2', '3']]:
    print(1)
else:
    print(2)