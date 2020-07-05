def search(arr,target,location):
    length = len(arr)
    mid = int(length/2)
    if length==1:
        if arr[0] == target:
            return location
        else:
            return -1
    if arr[mid]==target:
        return location+mid
    elif arr[mid]<arr[length-1]:
        if target>arr[mid] and target<=arr[length-1]:
            return search(arr[mid:],target,location+mid)
        else:
            return search(arr[:mid],target,location)
    else:
        if target<arr[mid] and target>=arr[0]:
            return search(arr[:mid],target,location)
        else:
            return search(arr[mid:],target,location+mid)


str = input()
target = int(input())
location = 0
arr = str.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
print(search(arr,target,location))



