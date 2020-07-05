arr1=input("")
arr2=input("")
maximum=0
for i in range(len(arr1)):
    for j in range(i+1,len(arr1)):
        exp=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        maximum=max(maximum,exp)
print(maximum)