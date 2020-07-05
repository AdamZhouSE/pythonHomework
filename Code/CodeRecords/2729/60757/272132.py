arr=list(eval(input()))
n=len(arr)//2
for i in range(n):
    if arr.count(arr[0])==2:
        tmp=arr[0]
        del arr[0]
        del arr[arr.index(tmp)]
    else:
        break
print(arr[0])