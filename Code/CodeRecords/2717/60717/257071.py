list1=eval(input())
flag=0
list2=list1.copy()
for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i][1]=='=' and list1[j][1]=='=':
            list3=[list1[i][0],list1[i][3]]
            list4=[list1[j][0],list1[j][3]]
            list3.sort()
            list4.sort()
            if list3 != list4:
                if list3[0]==list4[1]:
                    list2.append(list3[1]+'=='+list4[0])
                elif list3[0]==list4[0]:    
                    list2.append(list3[1]+'=='+list4[1])
                elif list3[1]==list4[0]:    
                    list2.append(list3[0]+'=='+list4[1])
                elif list3[1]==list4[1]:    
                    list2.append(list3[0]+'=='+list4[0])
for i in list1:
    str1=i[0]+'=='+i[3]
    str2=i[0]+'!='+i[3]
    str3=i[3]+'=='+i[0]
    str4=i[3]+'!='+i[0]
    if str1 in list2 and str2 in list2:
        flag=1
    if str1 in list2 and str4 in list2:
        flag=1
    if str3 in list2 and str2 in list2:
        flag=1
    if str3 in list2 and str4 in list2:
        flag=1
if flag == 1:
    print('false')
else:
    print('true')