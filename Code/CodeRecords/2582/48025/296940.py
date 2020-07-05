arr1=eval(input())
arr2=eval(input())
max=0

for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        temp_max=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        if(temp_max>max):
            max=temp_max
print(max)