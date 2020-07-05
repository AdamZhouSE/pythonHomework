arr=eval(input())
h=0
for i in range(0,len(arr)):
    value,n=arr[i],1
    for j in range(0,len(arr)):
        if i==j:
            continue
        else:
            if arr[j]>=value:
                n+=1
    if n==value:
        if n>h:
            h=n
print(h)