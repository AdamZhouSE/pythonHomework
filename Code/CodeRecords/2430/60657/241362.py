a=input()
num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
sum1=input()
sum1=int(sum1)
num2=input()
arr2=input().split(' ')
arr2=[int(x) for x in arr2]
sum2=input()
sum2=int(sum2)
cons1=[]
cons2=[]
for i in range(len(arr1)-1):
    for k in range(i+1,len(arr1)):
        if arr1[i]+arr1[k]==sum1:
            cons1.append(arr1[i])
            cons1.append(arr1[k])
if len(cons1)==0:
    print(-1)
else:
    for i in range(len(cons1)//2):
        
        print(cons1[0],cons1[1],sum1)
        cons1=cons1[2:]


for i in range(len(arr2)-1):
    for k in range(i+1,len(arr2)):
        if arr2[i]+arr2[k]==sum2:
            cons2.append(arr2[i])
            cons2.append(arr2[k])
if len(cons2)==0:
    print(-1)
else:
    for i in range(len(cons2)//2):
        print(cons2[0],cons2[1],sum2)
        cons2=cons2[2:]

