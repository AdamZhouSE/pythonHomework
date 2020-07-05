def isDifferent(str1,str2):
    flag=0
    for i in str1:
        if i in str2:
            flag=1
    if flag==0:
        return True
    else:
        return False

list1=eval(input())
max1=0
for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        if isDifferent(list1[i],list1[j]):
            max1=max(max1,len(list1[i])*len(list1[j]))
print(max1)