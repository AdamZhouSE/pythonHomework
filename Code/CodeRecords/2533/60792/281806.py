s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list2=[]
list3=[]
for i in range(0,len(list1)):
    if list1[i]%2==0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
list2=list2+list3
print(list2)