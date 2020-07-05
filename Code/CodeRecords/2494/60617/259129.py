def reversePair():
    arr=eval(input())
    print(merge(arr, 0, len(arr)-1))
    

def merge(arr, l , r):
    count=0
    if l>=r:
        return count
    mid=(l+r)/2
    count+=merge(arr, l, mid)
    count+=merge(arr, mid+1, r)
    j=mid+1
    for i in range(l, mid+1):
        while j<=r and arr[i]>arr[j]*2:
            j+=1
        count+=j-(mid+1)
    sort(arr, l, r)
    return count

def sort(arr, l, r):
    temp=[]
    if l>=r:
        return 
    mid=(l+r)/2
    j=mid+1
    while l<=mid and j<=r:
        if arr[l]<=arr[j]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[j])
            r+=1
    while l<=mid:
        temp.append(arr[l])
        l+=1
    while j<=r:
        temp.append(arr[j])
        j+=1
    for i in range(0, len(temp)):
        arr[i]=temp[i]
    return 

if __name__=='__main__':
    reversePair()