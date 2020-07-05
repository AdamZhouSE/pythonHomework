size=int(input())
list1=input().split()
del list1[0]
list1=[int(list1[i]) for i in range(len(list1))]
list2=input().split()
del list2[0]
list2=[int(list2[i]) for i in range(len(list2))]
list1b=[]
list2b=[]
for i in range(len(list1)):
    list1b.append(list1[i])
for i in range(len(list2)):
    list2b.append(list2[i])

count=0
isF=True
while len(list1)>0 and len(list2)>0:
    count+=1
    if list1[0]>list2[0]:
        list1.append(list2[0])
        list1.append(list1[0])
    else:
        list2.append(list1[0])
        list2.append(list2[0])
    del list1[0]
    del list2[0]
    if (list1b==list1 and list2b==list2) or (list1b==list2 and list2b==list1):
        print(-1)
        isF=False
        break
if isF:
    if len(list1)==0:
        print(count,2)
    else:
        print(count,1)