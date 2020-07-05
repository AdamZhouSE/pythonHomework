arr1=list(input())
arr2=list(input())
m=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)>m:
            m=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        else:
            continue
print(m)