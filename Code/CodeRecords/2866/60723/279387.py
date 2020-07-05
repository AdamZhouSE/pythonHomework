num=int(input())
array=input().split()
count=0
result=1
i=0
ar=[]
for i in range(len(array)):
    if array[i]=='1':
        if count!=0:
            ar.append(count+1)
        count=0
    else:
        count=count+1
if count!=0:
    ar.append(count)
for i in range(1,len(ar)-1):
    result=result*ar[i]
if array[len(array)-1]=='1':
    result=result*ar[len(ar)-1]
if array[0]=='1':
    result=result*ar[0]
print(result)