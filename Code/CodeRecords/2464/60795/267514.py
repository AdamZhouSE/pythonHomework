k=int(input())
arr=[int(n) for n in input().split(',')]
result=-1
for i in range(0,len(arr)):
    if arr[i]==k:
        result=1
        break
if result==-1:
    for i in range(2,len(arr)+1):
        for j in range(0,len(arr)-i+1):
            index=j
            sum=0
            while index<j+i:
                sum=sum+arr[index]
                index+=1
            if sum==k:
                result=i
                break
        if result!=-1:
            break
print(result)
    
