def maxChunksToSorted(arr):
    res=0
    n=len(arr)
    tmp=arr.copy()
    tmp.sort()
    max_val=0
    for i in range(n):
        if arr[i]>max_val:
            max_val=arr[i]
        if tmp[i]==max_val:
            res+=1
            max_val=0
    return res
a=input().replace('[','').replace(']','').split(',')
b=[]
for i in a:
    b.append(int(i))
print(maxChunksToSorted(b))