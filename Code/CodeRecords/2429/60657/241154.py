a=input()
num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
num2=input()
arr2=input().split(' ')
arr2=[int(x) for x in arr2]
cons1=[]
for i in range(0,len(arr1)-1):
    for k in range(i+1,len(arr1)):
        if(arr1[k]>arr1[i]):
            cons1.append(arr1[k]-arr1[i])
cons1.sort()
print(cons1[-1])
cons2=[]
for i in range(0,len(arr2)-1):
    for k in range(i+1,len(arr2)):
        if(arr2[k]>arr2[i]):
            cons2.append(arr2[k]-arr2[i])
cons2.sort()
print(cons2[-1])