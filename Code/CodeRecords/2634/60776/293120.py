a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(", ")
for i in range(0,len(b)):
    b[i]=int(b[i])
k=int(input())
list1=[]
list2=[]
for i in range(0,len(b)-1):
    for j in range(i+1,len(b)):
        temp=[]
        temp.append(b[i])
        temp.append(b[j])
        list1.append(temp)
        list2.append(b[i]/b[j])
list2.sort()
for i in range(0,len(list1)):
    if list1[i][0]/list1[i][1]==list2[k-1]:
        print(list1[i])
        break