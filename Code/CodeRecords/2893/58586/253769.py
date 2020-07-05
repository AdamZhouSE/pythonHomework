arr=eval(input())
arr.sort()
count=1
index=-1
for i in range(1,len(arr)):
    if arr[i]==arr[i-1]:
        count+=1
    else:
        if count==1:
            index=i-1
            break
print(arr[index])