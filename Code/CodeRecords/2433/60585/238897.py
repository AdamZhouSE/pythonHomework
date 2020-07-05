arr=eval(input())
arr=sorted(arr,key=lambda x:x[0])
i=0
j=1
result=[]
temp=arr[0]
while (i<len(arr))&(j<len(arr)):
    if temp[1]<arr[j][0]:
       result.append(temp)
       i=j
       j+=1
       temp=arr[i]
    else:
        temp=[temp[0],arr[j][1]]
        i=j
        j+=1
if i!=len(arr):
    result.append(temp)
print(result)