a=input().split(',')
k=int(a[0])
n=int(a[1])
list1=[]
list2=[]
output=[]
for i in range(1,8):
    for j in range(i+1,9):
        for k in range(j+1,10):
            list3=[]
            list3.append(i)
            list3.append(j)
            list3.append(k)
            list1.append(list3)
            list2.append(i+j+k)
for i in range(0,len(list2)):
    if list2[i]==n:
        output.append(list1[i])
print(output)