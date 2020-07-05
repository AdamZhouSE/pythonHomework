arr=eval(input())

arr_sorted=sorted(arr)
min=0
for i in range(1,len(arr)+1):
    for j in range(0,len(arr)-i+1):
        arr1=sorted(arr[j:j+i])
        temp_arr=arr.copy()
        for k in range(j,j+i):
            temp_arr[k]=arr1[k-j]
        
        if(arr_sorted==temp_arr):
            if(min==0):
                min=i

print(min)
