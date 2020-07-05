n=int(input())
list1=input().split()
list2=[]
list3=[]
for i in range(0,n):
    list1[i]=int(list1[i])
    list2.append(list1[i])
    list3.append(list1[i])
for i in range(0,n):
    a=list1[i]
    while True:
        list2.remove(a)
        if a in list2:
            list3.remove(a)
        else:
            list2.append(a)
            break
print(len(list3))
strr=''
for i in list3:
    strr=strr+str(i)+' '
print(strr[:-1])
    