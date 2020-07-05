input()
list=input()
num=int(list[4])
list1=input()
list11=[]
list22=[]
list11=list1.split()
list2=input()
list22=list2.split()
for i in range(len(list22)):
    list11.append(list22[i])
for i in range(len(list11)):
    for j in range(len(list11)-i-1):
        if list11[j]>list11[j+1]:
            list11[j],list11[j+1]=list11[j+1],list11[j]
print(list11[num])