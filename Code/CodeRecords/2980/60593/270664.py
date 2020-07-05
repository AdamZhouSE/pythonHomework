str1=input()
list1=input().split(" ")
list2=list(str1)
if list1[0]=='D':
    list2.remove(list1[1])
    str1 = ''.join(list2)
    print(str1)
elif list1[0]=='I':
    ind=-1
    for i in range(len(str1)):
        if str1[i]==list1[1]:
            ind=i
    if(ind==-1):
        print(list)
    else:
        list2.insert(ind,list1[2])
        str1 = ''.join(list2)
    print(str1)
elif list1[0]=='R':
    str2=str1.replace(list1[1],list1[2])
    print(str2)
