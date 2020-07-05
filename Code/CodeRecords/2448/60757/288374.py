arr=sorted(eval(input()))[::-1]
for i in range(1,len(arr)+1):
    if i!=len(arr):
        if arr[i-1]<i:
            print(i-1)
            break
    else:
        if arr[i-1]<i:
            print(i-1)
            break
        else:
            print(i)
            break