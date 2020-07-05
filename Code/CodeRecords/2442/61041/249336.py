arr = sorted(eval(input()))
if len(arr)<2:
    print(0)
elif len(arr)==2:
    print(arr[1]-arr[0])
else:
    temp = 0
    for i in range(0,len(arr)-1):
        if temp<arr[i+1]-arr[i]:
            temp = arr[i+1]-arr[i]
    print(temp)