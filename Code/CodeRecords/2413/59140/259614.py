n=int(input())
start=int(input())
arr=list(range(0,pow(2,n)))
for i in range(len(arr)):
    arr[i]=arr[i]^(arr[i]>>1)
arr=arr[arr.index(start):]+arr[:arr.index(start)]
print(arr)