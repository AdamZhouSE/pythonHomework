arr=list(eval(input()))
arr.sort()
arr.reverse()
h=0
for i in range(0,len(arr)):
    if i+1>=arr[i] :
        if i<len(arr)-1:
            if i+1>arr[i+1]:
                h=arr[i]
                break
        else:
            h=arr[i]
            break
print(h)