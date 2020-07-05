arr=eval(input())
temp=0
counts=[]
for i in range(0,len(arr)-1):
    temp=0
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp+=1
    counts.append(temp)
counts.append(0)
print(counts)