arr1=input().split(',')
arr2=input().split(',')
result=0
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        record=abs((int)(arr1[i])-(int)(arr1[j]))+abs((int)(arr2[i])-(int)(arr2[j]))+abs(i-j)
        if(record>result):
            result=record
print(result)