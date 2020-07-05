arr=[1,2,3,4,1,5]
count=0
arr_re=arr[::-1]
ind=0
while(ind!=len(arr)-1):
    if arr.count(arr[ind])==1:
        ind=ind+1
        count=count+1
    else:
        if len(arr)-1-arr_re.index(arr[ind])>ind:
            ind=len(arr)-1-arr_re.index(arr[ind])
            count=count+1
        for i in range(ind):
            if arr[i]==arr[ind]:
                arr[i]=0
print(count)