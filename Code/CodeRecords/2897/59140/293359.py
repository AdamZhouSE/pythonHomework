arr=input()
arr=arr[1:len(arr)-1].split(",")
for i in range(len(arr)):
    arr[i]=arr[i][1:len(arr[i])-1]
maxlength=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if len(set(arr[i]+arr[j]))==len(arr[i])+len(arr[j]):maxlength=max(maxlength,len(arr[i])*len(arr[j]))
print(maxlength)