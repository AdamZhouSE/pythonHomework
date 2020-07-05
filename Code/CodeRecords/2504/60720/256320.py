list1=eval(input())
list0=[]
min=abs(list1[0][0])+abs(list1[0][1])
list0=[]
for i in range(1,len(list1)):
    if abs(list1[i][0])+abs(list1[i][1])<min:
        min=abs(list1[i][0])+abs(list1[i][1])
for i in range(1,len(list1)):
    if abs(list1[i][0])+abs(list1[i][1])==min:
        list0.append(list1[i])
print(list0)
    