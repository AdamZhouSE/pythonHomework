def func(arr:list):
    if len(arr)==0:
        return 0
    mini=min(arr)
    indexofmin=arr.index(mini)
    arr2=arr[0:indexofmin+1]
    if indexofmin==len(arr)-1:
        return 1
    arr3=arr[indexofmin+1:]
    arr2.sort()
    if max(arr2)<min(arr3):
        return 1+func(arr3)
s=input()
lists=list(map(int,s[1:len(s)-1].split(',')))
print(func(lists))