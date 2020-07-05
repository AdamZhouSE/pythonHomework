list=input().split(',')
if len(list)==1:
    print(list[0])
elif len(list)==2:
    str=''
    str=list[0]+'/'+list[1]
    print(str)
else:
    list1=[]
    for i in range(len(list)-1):
        list1.append(list[i])
        list1.append('/')
        if i==0:
            list1.append('(')
    list1.append(list[-1])
    list1.append(')')
    print(''.join(list1))