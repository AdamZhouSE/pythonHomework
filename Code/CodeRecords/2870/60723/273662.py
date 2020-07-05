n=int(input())
temp=input().split()
array1=[]
array2=[]
for i in range(n):
    if int(temp[i])%2==0:
        array2.append(int(temp[i]))
    else:
        array1.append(int(temp[i]))
array1.sort()
if len(array1)%2==1:
    array1.pop(0)
total=0
for i in range(len(array1)):
    total=total+array1[i]
for i in range(len(array2)):
    total=total+array2[i]
print(total)