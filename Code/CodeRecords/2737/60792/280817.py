s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
n=len(list1)//3
list2=[]
for i in range(0,len(list1)):
    if list1.count(list1[i])>n:
        if list1[i] not in list2:
            list2.append(list1[i])
print(list2)