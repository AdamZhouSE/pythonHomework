arr=eval(input())
start=0
end=0
startDone=False
endDone=False
for i in range(0,len(arr)):
    smallest=min(arr[i:])
    smallestIndex=arr.index(smallest)
    biggest=max(arr[:len(arr)-i])
    biggestIndex=arr.index(biggest)
    if startDone==False:
        if smallestIndex!=i:
            start=i
            startDone=True
    if endDone==False:
        if biggestIndex!=len(arr)-1-i:
            end=len(arr)-1-i
            endDone=True
print(end-start+1)