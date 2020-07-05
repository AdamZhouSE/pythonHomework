arr=input()
arr=arr[1:len(arr)-1]
arr=list(map(int,arr.split(',')))
arr.sort()
if len(arr)<2:
    print(0)
else:
    i=-1
    for j in range(1,len(arr)):
        i=max(i,arr[j]-arr[j-1])
    print(i)