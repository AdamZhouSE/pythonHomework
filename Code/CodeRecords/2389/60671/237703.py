time=int(input())
length=int(input())
str1=input()
list1=str1.split()
list2=[]
for n in list1:
    list2.append(int(n))
list2.sort()
for i in range(int(length/2)):
    temp=list2[2*i]
    list2[2*i]=list2[2*i+1]
    list2[2*i+1]=temp
list3=[]
for n in list2:
    list3.append(str(n))
    
strr=" ".join(list3)
print(strr)