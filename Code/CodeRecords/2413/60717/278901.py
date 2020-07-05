n=int(input())
start=int(input())
list1=['0','1']
while n>1:
    n-=1
    list2=[]
    for i in list1:
        tmp='0'+i
        list2.append(tmp)
    for i in range(0,len(list1)):
        tmp='1'+list1[len(list1)-1-i]
        list2.append(tmp)
    list1=list2.copy()
index=0
for i in range(0,len(list1)):
    tmp='0b'+list1[i]
    if int(tmp,2)==start:
        index=i
        break
list3=[]
for i in range(0,len(list1)):
    tmp='0b'+list1[index]
    list3.append(int(tmp,2))
    index+=1
    if index==len(list1):
        index=0
print(list3)