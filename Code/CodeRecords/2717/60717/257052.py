list1=eval(input())
flag=0
for i in list1:
    str1=i[0]+'=='+i[3]
    str2=i[0]+'!='+i[3]
    str3=i[3]+'=='+i[0]
    str4=i[3]+'!='+i[0]
    if str1 in list1 and str2 in list1:
        flag=1
    if str1 in list1 and str4 in list1:
        flag=1
    if str3 in list1 and str2 in list1:
        flag=1
    if str3 in list1 and str4 in list1:
        flag=1
if flag == 1:
    print('false')
else:
    print('true')