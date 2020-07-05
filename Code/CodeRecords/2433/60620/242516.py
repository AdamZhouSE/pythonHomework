arr=sorted(eval(input()))
left=arr[0][0]
right=arr[0][1]
result=[]
for i in range(1,len(arr)):
    if((arr[i][0]<=right) and (arr[i][1]>right)):
        right=arr[i][1]
    else:
        result.append([left,right])
        left=arr[i][0]
        right=arr[i][1]
result.append([left,right])
print(result)
        
        

    