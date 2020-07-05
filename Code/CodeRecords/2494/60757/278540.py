arr=eval(input())
count=0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>2*arr[j]:
            count=count+1
print(count)