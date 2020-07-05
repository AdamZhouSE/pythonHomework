arr=eval(input())
max=0
for i in range(0,len(arr)):
    index=1
    com=arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]>com:
            index+=1
            com=arr[j]
    if index>max:
        max=index
print(max)
