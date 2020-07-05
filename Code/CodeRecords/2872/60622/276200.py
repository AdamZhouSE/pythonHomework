n=int(input())
arr=list(input())
count=0
for i in range(0,len(arr)-1):
    if arr[i]==arr[i+1]:
        count+=1
print(count)