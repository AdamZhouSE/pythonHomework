n=int(input())
arr=[int(x) for x in input().split(" ")]
arr.sort()
heapnum=0
while arr:
    temp= [arr[0]]
    arr.remove(arr[0])
    res=arr.copy()
    for i in range(len(arr)):
        if arr[i]>=len(temp):
            temp.append(arr[i])
            res.remove(arr[i])
    arr=res.copy()
    heapnum+=1
print(heapnum)