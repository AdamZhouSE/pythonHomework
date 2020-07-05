n=int(input())
str=input()
list1=str.split( )
temp=[]
for i in list1:
    temp.append(int(i))
list2=[]
temp.reverse()
for i in range(0,len(temp)):
    if(temp[i] in list2):
        k=1
    else:
        list2.append(temp[i])
list2.reverse()
print(len(list2))
for i in range(0,len(list2)):
    if(i!=len(list2)-1):
        print("{0} ".format(list2[i]),end="")
    else:
        print(list2[i])




