import math
arr=input("")
arr=arr.replace("[","")
arr=arr.replace("]","")
arr=list(map(int,arr.split(",")))
arr.sort()
i=1
maxlen=1
templen=1
while(i<len(arr)):
    if(arr[i]==arr[i-1]+1):
        templen=templen+1
    else:
        maxlen=max(templen,maxlen)
        templen=1
    i=i+1
print(maxlen)