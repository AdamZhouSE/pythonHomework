arr=eval(input())
sortedArr=sorted(arr)
low=count=0
high=1
while low<len(arr):
    if arr[low]==sortedArr[low]:
        count+=1
        low+=1
        high+=1
    else:
        high+=1
        while sorted(arr[low:high])!=sortedArr[low:high]:
            high+=1;
        low=high
        high+=1
        count+=1
print(count)