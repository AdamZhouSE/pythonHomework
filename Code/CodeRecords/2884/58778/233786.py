str1=input("")
list1=str1.split( )
x=int(list1[0])
d=int(list1[1])
str2=input()
list2=str2.split( )
list3=[]
for s in list2:
    list3.append(int(s))
count=0
for i in range(0,len(list3)-1):
    for j in range(i+1,len(list3)):
        if(abs(list3[j]-list3[i])<=d):
            count=count+1
print(count*2)