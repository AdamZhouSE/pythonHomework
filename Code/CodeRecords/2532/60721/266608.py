import re
def maxChunksToSorted(arr):
    res=0
    n=len(arr)
    tmp=arr.copy()
    tmp.sort()
    max_val=0
    for i in range(n):
        if arr[i]>max_val:
            max_val=arr[i]
        if i==n-1:
            res+=1
        else:
            if tmp[i]==max_val and min(arr[i+1:])>=max_val:
                res+=1
                max_val=0
    return res
s=re.findall("\d+",input())
s=[int(i) for i in s]
print(maxChunksToSorted(s))