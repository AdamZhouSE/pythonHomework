def find_min():
    arr = eval("[" + input() + "]")
    if len(arr)==1:
        print(arr[0])
        exit()
    if arr[len(arr)-1]>arr[0]:
        print(arr[0])
        exit()
    l=0
    r=len(arr)
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>arr[mid+1]:
            print(arr[mid+1])
            exit()
        elif arr[mid]<arr[mid-1]:
            print(arr[mid])
            exit()
        if arr[mid]>=arr[l]:
            l=mid+1
        else:
            r=mid-1

if __name__=='__main__':
    find_min()