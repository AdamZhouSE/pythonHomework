a=input()
num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
num2=input()
arr2=input().split(' ')
arr2=[int(x) for x in arr2]
odd1=[]
even1=[]
odd2=[]
even2=[]
for i in range(len(arr1)):
    if(arr1[i]%2==0):
        even1.append(arr1[i])
    else:odd1.append(arr1[i])
odd1.sort()
odd1.reverse()
even1.sort()
cons1=odd1+even1
cons1=[str(x) for x in cons1]

for i in range(len(arr2)):
    if(arr2[i]%2==0):
        even2.append(arr2[i])
    else:odd2.append(arr2[i])
odd2.sort()
odd2.reverse()
even2.sort()
cons2=odd2+even2
cons2=[str(x) for x in cons2]
print(' '.join(cons1)+' ')
print(' '.join(cons2)+' ')