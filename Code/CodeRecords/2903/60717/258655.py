def isDifferent(str1,str2):
    flag=1
    for i in str1:
        for j in str2:
            if i==j:
                flag=0
    if flag==1:
        return True
    else:
        return False

list1=eval(input())
maxx=0
for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        if isDifferent(list1[i],list1[j]):
            list1.append(list1[i]+list1[j])
for i in list1:
    maxx=max(maxx,len(i))
print(maxx)