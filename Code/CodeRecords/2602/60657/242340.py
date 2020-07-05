arr1=input()
arr1=arr1[1:-1]
arr1=arr1.split(',')
arr1=[int(x) for x in arr1]
arr2=input()
arr2=arr2[1:-1]
arr2=arr2.split(',')
arr2=[int(x) for x in arr2]
cons1=[]
for i in range(len(arr1)):
    for k in range(i,len(arr1)):
           cons1.append(arr1[i:k+1])
temp1=[]
temp2=[]
cons2=[]
for i in range(len(cons1)):
    if(cons1.count(cons1[i])==1):
        temp1.append(cons1[i])
for i in range(len(arr2)):
    for k in range(i,len(arr2)):
           cons2.append(arr2[i:k+1])
temp2=[]
final=[]
for i in range(len(cons2)):
    if(cons2.count(cons2[i])==1):
        temp2.append(cons2[i])
for i in range(len(temp2)):
    for k in range(len(temp1)):
        if(temp1[k]==temp2[i]):
            final.append(len(temp2[i]))
print(max(final))