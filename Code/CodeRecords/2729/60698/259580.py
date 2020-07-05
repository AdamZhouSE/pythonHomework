arr=list(eval(input()))
left=0
right=len(arr)
even_pair=((len(arr)//2)%2)==0
while True:
    mid=(left+right)//2
    if mid<len(arr)-1 and arr[mid]==arr[mid+1]:
        if even_pair:
            left=mid
            continue
        else:
            right=mid
            continue
    elif mid>0 and arr[mid]==arr[mid-1]:
        if even_pair:
            right=mid
            continue
        else:
            left=mid
            continue
    else :
        break
print(arr[mid])

