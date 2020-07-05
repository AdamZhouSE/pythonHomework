arr=eval(input())
maxlen,count = 0,1
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        count += 1
    else:
        maxlen=max(count,maxlen)
        count=1
maxlen=max(maxlen,count)
print(maxlen)