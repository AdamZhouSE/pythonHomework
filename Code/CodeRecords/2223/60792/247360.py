list1=list(input().split(","))
list2=[]
for i in range(0,len(list1)+1):
    list2.append(0)
list3=[0 for x in range(0,2)]
for i in range(0,len(list1)):
    n=int(list1[i])
    list2[n]=list2[n]+1
for i in range(1,len(list2)):
    if(list2[i]==2):
        list3[0]=i
    if(list2[i]==0):
        list3[1]=i
print(list3)
    