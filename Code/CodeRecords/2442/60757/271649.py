arr=sorted(eval(input()))
maxnum=0
if len(arr)<2:
    print('0')
else:
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]>maxnum:
            maxnum=arr[i+1]-arr[i]        
    print(maxnum)